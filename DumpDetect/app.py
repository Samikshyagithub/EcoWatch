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

app = Flask(__name__)


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

    # # load a pretrained YOLOv8n model
    # model = YOLO("mydrive/results/train/weights/best.pt","v8")

    # Vals to resize video frames | small frame optimise the run
    frame_wid = 640
    frame_hyt = 480
    
    cap = cv2.VideoCapture(video_path)
    counter=0
    carry_record=[0,0,0]