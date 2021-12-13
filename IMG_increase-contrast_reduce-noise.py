# Python script to increase image contrast and to reduce noise
# intended as pre-processing for text scans to be read with Transkribus OCR

from PIL import Image, ImageEnhance 
import os
import cv2
import numpy

path="C:\\Users\\####\\Staatskalender1740_PNG"
target="C:\\Users\\####\\Staatskalender1740_PNG_contrast2_noise"

count=0
for f in os.listdir(path):
    count+=1
    im_path=os.path.join(path, f)
    print(im_path)
    im=Image.open(im_path)
    
# enhance contrast with PIL

    enhancer=ImageEnhance.Contrast(im)
    enhanced_im=enhancer.enhance(2.0)
    print(type(enhanced_im)) 

# image class needs to be change from PIL image object to Open CV image object

    opencv_im=cv2.cvtColor(numpy.array(enhanced_im), cv2.COLOR_RGB2BGR) # transform colour encoding

# use median blur function from Open CV library suitable for colour images
# cf. test with different noise filters on https://towardsdatascience.com/image-filters-in-python-26ee938e57d2
   
    new_image=cv2.medianBlur(opencv_im, 5) # 2nd position = kernel size
    cv2.imwrite(os.path.join(target, "%s.png" % count), new_image) 

print("done")
