#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2
import zbar
import PIL.Image

#initialize CV2
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Heigh
cap.set(5, 5)   # FPS
if cap.isOpened() is False:
    raise("IO Error")

#initialize QR_Code
scanner = zbar.ImageScanner()
scanner.parse_config('enable')


while True:
    #input image
    ret, img = cap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    #grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Binarization
#    tresh = 100
    max_pixel = 255
#    ret, img_thre = cv2.threshold(img_gray, tresh, max_pixel, cv2.THRESH_BINARY)
    img_thre = cv2.adaptiveThreshold(img_gray, max_pixel, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
    #二値化にガウシアンフィルタを追加した
    
    
    #picture change PIL
    pil_img = PIL.Image.fromarray(img_thre)
    width, height = pil_img.size
    raw = pil_img.tobytes()
    image = zbar.Image(width, height, 'Y800', raw)

    #result
    
    print image
    scanner.scan(image)
    for symbol in image:
        print symbol.data
        
        
    cv2.imshow('QR reader', img_thre)
    #finish flag
    k = cv2.waitKey(10)
    if k == 27: #ESC
        break;

cap.release()
cv2.destroyAllWindows()