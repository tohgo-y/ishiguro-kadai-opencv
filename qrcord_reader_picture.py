#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2
import zbar
import PIL.Image



img = cv2.imread('/home/gura101/Pictures/many_qrcode.jpg')

#initialize QR_Code
scanner = zbar.ImageScanner()
scanner.parse_config('enable')



#grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Binarization
max_pixel = 255
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
k = cv2.waitKey(0)
if k == 27: #ESC
    cv2.destroyAllWindows()

#cap.release()
