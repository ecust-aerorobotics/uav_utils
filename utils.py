# use open cv to show new images from AirSim 

from AirSimClient import *
# requires Python 3.5.3 :: Anaconda 4.4.0
# pip install opencv-python
import cv2
import time
import sys
from PIL import Image

def getScreenDepthVis(client):

    responses = client.simGetImages([ImageRequest(0, AirSimImageType.DepthPerspective, True, False)])
    img1d = np.array(responses[0].image_data_float, dtype=np.float)
    img1d = 255/np.maximum(np.ones(img1d.size), img1d)
    img2d = np.reshape(img1d, (responses[0].height, responses[0].width))
    
    image = np.invert(np.array(Image.fromarray(img2d.astype(np.uint8), mode='L')))
    
    factor = 10
    maxIntensity = 255.0 # depends on dtype of image data
    
    # Decrease intensity such that dark pixels become much darker, bright pixels become slightly dark 
    newImage1 = (maxIntensity)*(image/maxIntensity)**factor
    newImage1 = np.array(newImage1,dtype=np.uint8)
    
    #cv2.imshow("Test", newImage1)
    #cv2.waitKey(0)
    
    return newImage1
