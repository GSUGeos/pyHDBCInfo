import cv2 #Read image / camera/video input
from tabulate import tabulate
from pyzbar.pyzbar import decode
import sys
import csv

used_codes = []
dict= {}
cap = cv2.VideoCapture (0)
cap.set (3, 640) #3 - Width
cap.set (4, 480) #4 - Height
camera = True
while camera == True:
    success, frame = cap.read()

    for code in decode(frame) :

        if code.data.decode('utf-8') not in used_codes:
            if code.type == "CODE128":
                test = code.data.decode('utf-8')
                try:
                    HDD, S_N = test.split("-")
                except (ValueError):
                    S_N = test
                    used_codes.append(S_N)
                    with open (sys.argv[1], "a") as file:
                        writer = csv.DictWriter (file, fieldnames=["Manufacturer Name", "S/N", "MDL"])
                        writer.writerow({"S/N":S_N})
                else:
                    used_codes.append(S_N)
                    if HDD == "WD":
                        MN = "Western Digital"
                        with open (sys.argv[1], "a") as file:
                            writer = csv.DictWriter (file, fieldnames=["Manufacturer Name", "S/N", "MDL"])
                            writer.writerow({"Manufacturer Name":MN, "S/N":S_N})
                    
                
            if code.type == "CODE39":
                used_codes.append(MDL)
                MDL = code.data.decode('utf-8')
                with open (sys.argv[1], "a") as file:
                    writer = csv.DictWriter (file, fieldnames=["Manufacturer Name", "S/N", "MDL"])
                    writer.writerow({"MDL":MDL})


    cv2.imshow('Testing-code-scan', frame)
    cv2.waitKey(1)