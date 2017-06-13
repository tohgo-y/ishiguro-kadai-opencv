# -*- coding: utf-8 -*-
import numpy as np
import cv2


def main():
    
    cascade_path = "/home/gura101/.pyenv/versions/anaconda3-4.1.1/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"
    color = (255, 255, 255) # color of rectangle for face detection
    fontType = cv2.FONT_HERSHEY_SIMPLEX
    
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)
    cam.set(4, 480)
    cam.set(5, 10)
    
    count=0
    
    while True:
        ret, capture = cam.read()
        
        if not ret:
            print('error')
            break
        count += 1
        if count > 1:
            image = capture.copy()
            #print("picture size is {0}".format(image.shape[:2]))
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cascade = cv2.CascadeClassifier(cascade_path)
            facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.11, minNeighbors=3, minSize=(50, 50))
            
            ##detectMultiScale関数の返り値は顔の資格の各座標？
            ##scalefactor は顔認識の制度を上げる?
            ##minineighborは矩形の近傍いくつ分を採用するかということ
    
            if len(facerect) > 0:
                i = 0
                for rect in facerect:
                    cv2.rectangle(image, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=5)
                    
                    
                    
                    cen = rect[0:2]+rect[2:4]*0.5
                    cen = cen.astype(np.int64)      #顔の中心座標
                    
                    #print("rect is {0}".format(rect[3]))
                    
                    if i == 0:
                        unicen = cen
                        facesize = rect[2]
                    elif (i > 0) and (rect[2] > facesize):
                        unicen = cen    
                        facesaize = rect[2]
                    i = i + 1
                    
                    #tupleは座標だから(x,y)だよな
                    #rect [w x y z] は1,2番目が顔の左上画像、3,4番目がx,y方向の距離
                    
                    
            
                cv2.circle(image, tuple(unicen), 20, color, thickness = 2) 
                cv2.putText(image, "Face_Width " + str(rect[2]), tuple(rect[0:2]), fontType, 0.5, (100, 100, 100),1)               
                print("Center of gravity is ({0})".format( unicen ))
                #print("rect is {0}".format(rect[3]))
            
    
            count=0
            cv2.imshow('face detector', image)
            #10msecキー入力待ち
            k = cv2.waitKey(10)
            #Escキーを押されたら終了
            if k == 27:
                break
            
    
    
    cam.release()
    cv2.destroyAllWindows()
    
    
    
    
if __name__ == '__main__':
    main()