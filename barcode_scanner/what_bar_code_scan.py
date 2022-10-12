import cv2 #Read image / camera/video input
from tabulate import tabulate
from pyzbar.pyzbar import decode
import sys
import csv

used_codes = []
cap = cv2.VideoCapture (0)
cap.set (3, 640) #3 - Width
cap.set (4, 480) #4 - Height
camera = True
while camera == True:
    success, frame = cap.read()
    
   
    for code in decode(frame) :
        if code.data.decode('utf-8') not in used_codes:
            used_codes.append(code.data.decode('utf-8'))
            #if len(code.data.decode('utf-8')) == 8:
            print (code)            
                        
    cv2.imshow('Testing-code-scan', frame)
    cv2.waitKey(1)