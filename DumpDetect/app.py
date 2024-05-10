import cv2
import winsound 
import time
import os
import random
import numpy as np
from ultralytics import YOLO
import cv2
from datetime import datetime
from vidgear.gears import CamGear,WriteGear
from pygame import mixer
from flask import Flask, render_template, request, redirect, send_file, url_for, Response, jsonify
import psycopg2
import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request,send_from_directory
from flask_mail import Mail, Message
import base64
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import math
import cvzone
from flask_cors import CORS
app = Flask(__name__)

CORS(app, origins='http://localhost:3000')

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

def predict2(video_path):
    class_list=["fire"]
    detection_colors=[]
    for i in range(len(class_list)):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        detection_colors.append((r, b, g))
        
    # load a pretrained YOLOv8n model
    model = YOLO("fire.pt","v8")
    
    # Vals to resize video frames | small frame optimise the run
    frame_wid = 640
    frame_hyt = 480

    # cap = cv2.VideoCapture(1)
    
    cap = cv2.VideoCapture(video_path)

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
        CREATE TABLE IF NOT EXISTS fire (
            filename TEXT PRIMARY KEY NOT NULL
        );
    """)

    conn.commit()
    cur.close()
    
    while True:
        ret,frame = cap.read()
        if not ret:
            break
        
        frame = cv2.resize(frame,(640,480))
        result = model(frame,stream=True)

        # Getting bbox,confidence and class names informations to work with
        for info in result:
            boxes = info.boxes
            for box in boxes:
                confidence = box.conf[0]
                confidence = math.ceil(confidence * 100)
                Class = int(box.cls[0])
                if confidence > 50:
                    x1,y1,x2,y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1),int(y1),int(x2),int(y2)
                    cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),5)
                    cvzone.putTextRect(frame, f'{class_list[Class]} {confidence}%', [x1 + 8, y1 + 100], scale=1.5,thickness=2)
                    now=datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    font = cv2.FONT_HERSHEY_COMPLEX
                    # cv2.putText(frame,"KU,Dhulikhel",(0,50),font,1,(255, 0, 0),2)
                    cv2.putText(frame,current_time,(0,100),font,1,(255, 255, 255),2)
                    
                    now=datetime.now()
                    folder_name=now.strftime("%Y%m%d")
                    file_name = now.strftime("%H%M%S")
                    firedetect_folder = f'firedetect\{folder_name}'
                    if not os.path.isdir(firedetect_folder):
                        os.mkdir(firedetect_folder)
                    firedetect_path = os.path.join(firedetect_folder, f"{file_name}.jpg")
        
                    # Check if firedetect_path already exists
                    if not os.path.exists(firedetect_path):
                        # Save image to firedetect folder
                        cv2.imwrite(firedetect_path, frame)
                        
                        # Insert filename into table
                        cur = conn.cursor()
                        cur.execute(f"INSERT INTO fire(filename) VALUES ('firedetect/{file_name}.jpg')")
                        conn.commit()
                        
                        # Play alert sound
                        mixer.init()
                        sound = mixer.Sound("alert.wav")
                        sound.play()
                        
                        # Stop processing the video
                        cap.release()
                        cv2.destroyAllWindows()
                        return 
                    else:
                        # Firedetect_path already exists, skip saving image
                        print(f"Image {firedetect_path} already exists. Skipping saving.")
                        #Return response
                
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()
            yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

    
    
    
def predict1(video_path): 
    # opening the file in read mode
    my_file = open("class.txt", "r")
    # reading the file
    data = my_file.read()
    # replacing end splitting the text | when newline ('\n') is seen.
    class_list = data.split("\n")
    my_file.close()

    
    attachpath = None
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

    # cap = cv2.VideoCapture(1)
    
    cap = cv2.VideoCapture(video_path)

    # cap = CamGear(
    # source=video_path,
    # stream_mode=True,
    # logging=True).start()

    # if not cap.isOpened():
    #     print("Cannot open video")
    #     exit()

    counter=0
    carry_record=[0,0,0]

    # frames=[]


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
                # print(i)

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
                        # print("Start")
                        # print(carry_record)
                        # print(f"Counter:{counter} | Obj_count= {obj_count}")
                        # print("End")
                        if carry_record[-2]==1 and counter<obj_count:
                            counter=counter+1
                            now = datetime.now()

                            # format the time as a string
                            file_name = now.strftime("%H%M%S")
                            folder_name = now.strftime("%Y%m%d")
                            attachpath=f"suspects/{folder_name}/{file_name}.jpg"
                            print(file_name,folder_name,attachpath,attachpath)
                            if not os.path.isdir('suspects/'+folder_name):
                                os.mkdir('suspects/'+folder_name)
                            print(attachpath)
                            cv2.imwrite(attachpath,frame)
                            
                            # print(attachpath)
                            # send_email_with_attachment("adamfirstman22@gmail.com", "abiraladhikari1222@gmail.com", "Garbage Dump Alert", "Somebody is dumping Garbage in your yard", attachpath, credentials_path='credentials.json')
                            cur = conn.cursor()
                            
                            cur.execute(f"INSERT INTO sessions(filename) VALUES ('suspects/{folder_name}/{file_name}.jpg')")
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




@app.route('/testurl/<path:input_url>',methods=['GET'])
def video(input_url):
    url= request.view_args['input_url']
    print(url)
    predict1(url)
    # return send_from_directory('static',imagepath)
    return Response(predict1(url),mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/getsuspects', methods=["GET"])
def get_all_suspects():
    folder_path = "suspects/20240510"

    # Get a list of all image files in the folder
    image_files = [file for file in os.listdir(folder_path) if file.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    # List to store image URLs
    image_urls = []

    # Iterate through image files and collect their URLs
    for image_file in image_files:
        image_url = f"http://127.0.0.1:5000/get_image/{image_file}"  # URL to retrieve the image
        image_urls.append(image_url)

    # Return image URLs as JSON
    return {"image_urls": image_urls}

@app.route('/getfire', methods=["GET"])
def get_all_fireinstance():
    folder_path = "firedetect/20240510"

    # Get a list of all image files in the folder
    image_files = [file for file in os.listdir(folder_path) if file.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    # List to store image URLs
    image_urls = []

    # Iterate through image files and collect their URLs
    for image_file in image_files:
        image_url = f"http://127.0.0.1:5000/get_fireimage/{image_file}"  # URL to retrieve the image
        image_urls.append(image_url)

    # Return image URLs as JSON
    return {"image_urls": image_urls}

@app.route('/get_fireimage/<path:image_filename>')
def get_fireimage(image_filename):
    folder_path = "firedetect/20240510"
    # Return the requested image file
    return send_from_directory(folder_path, image_filename)
    
@app.route('/get_image/<path:image_filename>')
def get_image(image_filename):
    folder_path = "suspects/20240510"
    # Return the requested image file
    return send_from_directory(folder_path, image_filename)
    

    
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

@app.route('/firedetect',methods=['GET'],endpoint='fire_detect_endpoint')
def firedetect():
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
        cur.execute("SELECT * FROM fire")

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
        results=jsonify(results)
        print(results)
        return results
    

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return jsonify({"error": "Failed to fetch data"}), 500
    
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/images/<path:filename>')
def get_image(filename):
    return send_file(os.path.join('suspects', filename))

@app.route('/fireimages/<path:filename>')
def get_image(filename):
    return send_file(os.path.join('suspects', filename))




app.run(port=5000)