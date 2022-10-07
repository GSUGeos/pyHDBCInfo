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
    
    with open (sys.argv[1], "a") as file:
        writer = csv.DictWriter (file, fieldnames=["Manufacturer Name", "S/N", "MDL"])
        #writer.writeheader()

        for code in decode(frame) :
            if code.data.decode('utf-8') not in used_codes:
                if code.type == "CODE128":
                    test = code.data.decode('utf-8')
                    try:
                        HDD, S_N = test.split("-")
                    except (ValueError):
                        used_codes.append(test)
                        pass
                    else:
                        used_codes.append(test)
                        used_codes.append(S_N)
                        if HDD == "WD":
                            MN = "Western Digital"
                  
                if code.type == "CODE39":
                    MDL = code.data.decode('utf-8')
                    used_codes.append(MDL)

                try:
                    writer.writerow({"Manufacturer Name":MN, "S/N":S_N, "MDL":MDL})
                except (NameError):
                    pass
                        
    cv2.imshow('Testing-code-scan', frame)
    cv2.waitKey(1)