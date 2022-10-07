import cv2 #Read image / camera/video input
from pyzbar.pyzbar import decode


dict = {"Manufacturer Name"}
used_codes = []
cap = cv2.VideoCapture (0)
cap.set (3, 640) #3 - Width
cap.set (4, 480) #4 - Height
camera = True
while camera == True:
    success, frame = cap.read()
    try:
        for code in decode(frame) :
            if code.data.decode('utf-8') not in used_codes:
                used_codes.append(code.data.decode('utf-8'))
                if code.type == "CODE128":
                    test = code.data.decode('utf-8')
                    HDD, S_N = test.split("-")
                    if S_N == "":
                        print (f"S/N: {code.data.decode('utf-8')}")
                    else:
                        if HDD == "WD":
                            MN = "Western Digital"
                            print (f"Manufacturer: {MN}")
                        print (f"S/N: {S_N}")
                if code.type == "CODE39":
                    print (f"MDL: {code.data.decode('utf-8')}")
    except:
        pass
        
        
    cv2.imshow('Testing-code-scan', frame)
    cv2.waitKey(1)