import cv2

citra = cv2.imread("D:/Citra/LOGO UNIB.png")
cv2.imshow("unib-0",citra[:,:,0])
cv2.imshow("unib-1",citra[:,:,1])
cv2.imshow("unib-2",citra[:,:,2])
print(citra[:,:,0])
print(citra[:,:,1])
print(citra[:,:,2])
cv2.waitKey()