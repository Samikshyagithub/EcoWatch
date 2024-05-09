import cv2
import winsound 
import time
import os
import random
import numpy as np
from ultralytics import YOLO
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from pygame import mixer
from flask import Flask, render_template, request, redirect, send_file, url_for, Response, jsonify
from flask import Flask, request
from flask_mail import Mail, Message
import psycopg2
import base64
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


app = Flask(__name__)

def create_message_with_attachment(sender, to, subject, message_text, file_path):

    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    msg = MIMEText(message_text)
    message.attach(msg)

    with open(file_path, 'rb') as fp:
        img_data = fp.read()

    image = MIMEImage(img_data, name=os.path.basename(file_path))
    message.attach(image)

    raw_message = base64.urlsafe_b64encode(message.as_bytes())
    raw_message = raw_message.decode()
    return {'raw': raw_message}

def send_email_with_attachment(sender_email, to_email, subject, message_text, file_path, credentials_path='credentials.json'):

    creds = Credentials.from_authorized_user_file(credentials_path)
    service = build('gmail', 'v1', credentials=creds)

    message = create_message_with_attachment(sender_email, to_email, subject, message_text, file_path)
    service.users().messages().send(userId='me', body=message).execute()


@app.get("/")
def read_root():
    return {"Hello": "World"}

def predict1(video_path): 
    # opening the file in read mode
    my_file = open("class.txt", "r")
    # reading the file
    data = my_file.read()
    # replacing end splitting the text | when newline ('\n') is seen.
    class_list = data.split("\n")
    my_file.close()

    
    
    # Generate random colors for class list
    detection_colors = []
    for i in range(len(class_list)):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        detection_colors.append((r, b, g))

    # load a pretrained YOLOv8n model
    model = YOLO("mydrive/results/train/weights/best.pt","v8")

    # Vals to resize video frames | small frame optimise the run
    frame_wid = 640
    frame_hyt = 480
    
    cap = cv2.VideoCapture(video_path)
    counter=0
    carry_record=[0,0,0]
    
    

    db_host = 'localhost'
    db_name = 'flasksql'
    db_user = 'postgres'
    db_pass = 'abiral'

    conn = psycopg2.connect(
        host = db_host,
        dbname = db_name,
        user = db_user,
        password = db_pass
    )

    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            filename TEXT PRIMARY KEY NOT NULL
        );
    """)

    conn.commit()
    cur.close()
    
    while True:

        
        # Capture frame-by-fame
        ret,frame = cap.read()
        # if frame is read correctly ret is Tru
        if not ret:
            break
        # Predict on image
        # frame_count=frame_count+1

        detect_params = model.predict(source=[frame], conf=0.30, save=False)
        carry_flag=0

        # Convert tensor array to numpy
        DP = detect_params[0].cpu().numpy()
        objects= np.array(detect_params[0].boxes.cls.cpu())
   
        obj_count=np.count_nonzero(objects ==1 )
        font = cv2.FONT_HERSHEY_COMPLEX
        now=datetime.now()
        current_time = now.strftime("%H:%M:%S")
        cv2.putText(frame,"KU,Dhulikhel",(0,50),font,1,(255, 0, 0),2)
        cv2.putText(frame,current_time,(0,100),font,1,(0, 0, 255),2)
        # time.sleep(1)

        if len(DP) != 0:

            
            for i in range(len(detect_params[0])):
                print(i)

                boxes = detect_params[0].boxes
                box = boxes[i]  # returns one box
                clsID = box.cls.cpu().numpy()[0]
            
                conf = box.conf.cpu().numpy()[0]
                bb = box.xyxy.cpu().numpy()[0]

                cv2.rectangle(
                    frame,
                    (int(bb[0]), int(bb[1])),
                    (int(bb[2]), int(bb[3])),
                    detection_colors[int(clsID)],
                    3,
                )

                if class_list[int(clsID)]=="carryload":
                        carry_record.append(1)
                       
                        carry_flag=1
                
                if class_list[int(clsID)]=="thrownwaste":
                        print("Start")
                        print(carry_record)
                        print(f"Counter:{counter} | Obj_count= {obj_count}")
                        print("End")
                        if carry_record[-2]==1 and counter<obj_count:
                            counter=counter+1
                            now = datetime.now()

                            # format the time as a string
                            file_name = now.strftime("%H%M%S")
                            folder_name = now.strftime("%Y%m%d")
                            if not os.path.isdir('suspects/'+folder_name):
                                os.mkdir('suspects/'+folder_name)
                            cv2.imwrite(f"suspects/{folder_name}/{file_name}.jpg",frame)
                            cur = conn.cursor()
                            
                            cur.execute(f"INSERT INTO sessions(filename) VALUES ('{folder_name}/{file_name}.jpg')")
                            conn.commit()
                            mixer.init() 
                            sound=mixer.Sound("alert.wav")
                            sound.play()
                            
                            # frame_num=int(cap.get(cv2.CAP_PROP_POS_FRAMES))
                            # frames.append(frame_num)

                # Display class name and confidence
                
                cv2.putText(
                    frame,
                    class_list[int(clsID)] + " " + str(round(conf, 3)*100) + "%",
                    (int(bb[0]), int(bb[1]) - 10),
                    font,
                    1,
                    (255, 255, 255),
                    2,
                )
                
            if carry_flag==0:
                carry_record.append(0)

        #Return response
        ret,buffer=cv2.imencode('.jpg',frame)
        frame=buffer.tobytes()

        yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    
    
    
app.route('/testurl/<path:input_url>',methods=['GET'])
def video(input_url):
    url= request.view_args['input_url']
    print(url)
    return Response(predict1(url),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/firetest/<path:fire>',methods=['GET'],endpoint='fire_test_endpoint')
def video(fire):
    fire_url= request.view_args['fire']
    print(fire_url)
    return Response(predict2(fire_url),mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/suspects')
def suspects():
    try:
        db_host = 'localhost'
        db_name = 'flasksql'
        db_user = 'postgres'
        db_pass = 'abiral'
        # connect to the PostgreSQL database
        conn = psycopg2.connect(
        host = db_host,
        dbname = db_name,
        user = db_user,
        password = db_pass
    )

        # create a cursor object
        cur = conn.cursor()

        # execute the SELECT statement
        cur.execute("SELECT * FROM sessions")

        # fetch all the rows
        rows = cur.fetchall()

        # convert the rows to a list of dictionaries
        results = []
        for row in rows:
            results.append({
                "file_name": row[0],
            })

        # close the cursor and connection
        
        conn.close()

        # return the results as JSON
        return jsonify(results)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return jsonify({"error": "Failed to fetch data"}), 500
