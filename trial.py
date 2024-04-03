import cv2
import numpy as np
import pytesseract
import sys
import timm
import torch
import urllib
from PIL import Image, ImageChops
import easyocr
import os
import imutils

#pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR'

class avi2jpg:
    vid = None
    def convert(self, video):
        vidcap = cv2.VideoCapture(video)
        success,image = vidcap.read()
        count = 0
        while success:
            framecount = "{number:06}".format(number=count) #188, 116
            image = image[0:94, 0:90]
            
            image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            image = np.array(trim(image))
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            fm = cv2.Laplacian(gray, cv2.CV_64F).var()
            print(fm)
            # if the focus measure is less than the supplied threshold,
            # then the image should be considered "blurry"
            thr = 1300
            if fm > thr:
                dir = 'trial_data/'
                cv2.imwrite(dir+framecount+".jpg", gray)     # save frame as JPEG file      
            success,image = vidcap.read()
            print('Read a new frame: ', success)
            count += 1
def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)
if __name__ == "__main__":
    if len(sys.argv) != 2:
        "If you don't give an argument to the call"
        # # Load the img
        reader = easyocr.Reader(['en']) # need to run only once to load model into memory
        filedir = "/home/general/Documents/work/computer-vision/trial_data/"
        
        thr = .90
        for i, filename in enumerate(os.listdir(filedir)):
            result = reader.readtext(filedir+filename, allowlist='0123456789')
            if result != []: #and result[0][2]> thr:
                print(filename, i, result)

    else:
        converter = avi2jpg()
        converter.convert(sys.argv[1])
   