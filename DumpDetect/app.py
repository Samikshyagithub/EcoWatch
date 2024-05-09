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