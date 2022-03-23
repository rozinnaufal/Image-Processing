import cv2
image = cv2.imread('D:\Citra\LOGO HITAM PUTIH HD.jpg')
cv2.imshow("Original", image)

#erotion
for i in range(0,3):
    eroded = cv2.erode(image.copy(), None, iterations = i + 1)
    cv2.imshow(f"Erosi{i+1} kali", eroded)
    cv2.waitKey(0)