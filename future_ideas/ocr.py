import easyocr
import cv2
from matplotlib import pyplot as py
import numpy as np

reader = easyocr.Reader(["en"], gpu=True)
vid = cv2.VideoCapture(0)

while True:
    success, frame = vid.read()
    result = reader.readtext(frame)
    if result[0][-2] == "GB":
        print (result[0][-3])
    