# -*- coding: utf-8 -*-
import numpy as np
import cv2


def main():
    
    cascade_path = "/home/gura101/.pyenv/versions/anaconda3-4.1.1/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"
    color = (255, 255, 255) # color of rectangle for face detection
    image = cv2.imread('/home/gura101/Pictures/group-shot.jpg')
    
    fontType = cv2.FONT_HERSHEY_SIMPLEX
    
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
            
            print("rectwidth[{0}] is {1}".format(i,rect[2]))
            
            if i == 0:
                unicen = cen
                facesize = rect[2]
                num = i
            elif (i > 0) and (rect[2] > facesize):
                unicen = cen  
                facesize = rect[2]  
                num = i
                
            cv2.putText(image, "Face_num " + str(i) + " Width " + str(rect[2]), tuple(rect[0:2]), fontType, 0.5, (100, 100, 100),1)
                
            i = i + 1
            
            #tupleは座標だから(x,y)だよな
            #rect [w x y z] は1,2番目が顔の左上画像、3,4番目がx,y方向の距離
            
            
            
    
        cv2.circle(image, tuple(unicen), 20, color, thickness = 2)                
        print("Center of gravity is ({0})".format( unicen ))
        print("Number of Face is {0}, facesize is {1}".format(num, facesize))
        #print("rect is {0}".format(rect[3]))
        
        

    cv2.imshow('face detector', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

    
    
    
if __name__ == '__main__':
    main()