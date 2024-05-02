import cv2
import numpy as np
# import pytesseract
import sys
# import timm
import torch
import urllib
from PIL import Image, ImageChops
# import easyocr
import os
# import imutils
import json

#pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR'

dir = 'trial_data'
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
    def spliter(self, video):
        anno = {}
        anno["images"] = []
        vidcap = cv2.VideoCapture(video)
        success,image = vidcap.read()
        count = 1
        while success:
            framecount = "{number:06}".format(number=count) #188, 116
            # if the focus measure is less than the supplied threshold,
            # then the image should be considered "blurry"
            sfile = f"{dir}/{video.split('/')[-1]}"
            os.makedirs(sfile, exist_ok=True)
            cv2.imwrite(f"./{sfile}/{framecount}.jpg", image)     # save frame as JPEG file      
            success, image = vidcap.read()
            if not success:
                break
            anno["images"].append({
                "id": count,
                "frame_id": count,
                "prev_image_id": count - 1 if count > 1 else -1,
                "next_image_id": count + 1,
                "video_id": 1,
                "height": image.shape[0],
                "width": image.shape[1]
            })
            print('Read a new frame: ', success)
            count += 1
        json.dump(anno, open(os.curdir + f"/{dir}/annotations/{video.split('/')[-1]}.json", "w"))
def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

if __name__ == "__main__":
        converter = avi2jpg()
        converter.spliter(sys.argv[1])
   