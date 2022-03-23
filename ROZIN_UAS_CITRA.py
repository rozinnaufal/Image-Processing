#from scipy import ndimage
import cv2
import numpy as np
#image = cv2.imread('D:\Citra\LOGO UNIB.png')
#cv2.imshow("Original", image)

def sobel (img):
    im =  img.astype('int32')

    gx = scipy.sobel(im, 1)
    gy = scipy.sobel(im, 0)

    magnitude = np.hypot(gx, gy)
    magnitude *= 255.0 / np.max(magnitude)

    cv2.imwrite('sobel.jpg', magnitude) 

def prewitt(img):
    pass

#def canny (img):
    pass
    image = cv2.imread('D:\Citra\Botak.jpg', 0)
    sobel(image)
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    cv2.waitKey()