import cv2 #Read image / camera/video input
from pyzbar.pyzbar import decode




used_codes = []

def main():
    
    
    print (getS_N())

    

def getS_N():
    unfilteredS_N = []
    unfiltered_MDL = []
    global used_codes
    cap = cv2.VideoCapture (0)
    cap.set (3, 640) #3 - Width
    cap.set (4, 480) #4 - Height
    camera = True

    while camera == True:
        success, frame = cap.read()
        for code in decode(frame) :
            if code.data.decode('utf-8') not in used_codes:
                used_codes.append(code.data.decode('utf-8'))
                if code.type == "CODE128":
                    unfilteredS_N.append(code.data.decode('utf-8'))
                if code.type == "CODE39":
                    unfiltered_MDL.append(code.data.decode('utf-8'))
        if len(unfiltered_MDL) == 1 and len(unfilteredS_N) == 1:
            return unfilteredS_N, unfiltered_MDL
            
if __name__ == "__main__":
    main()