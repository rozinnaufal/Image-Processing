import numpy as np
import cv2
import numpy as np
image = cv2.imread('D:\Citra\LOGO UNIB.png')
#cv2.imshow("Original", image)
def gaussian_kernel(size, sigma=1):
    size = int(size) // 2
    x, y = np.mgrid[-size:size+1, -size:size+1]
    normal = 1 / (2.0 * np.pi * sigma**2)
    g =  np.exp(-((x**2 + y**2) / (2.0*sigma**2))) * normal
    return g
cv2.imshow(f"Dilasi{i+1} kali", dilated)
#    cv2.waitKey(0)
cv2.waitKey()