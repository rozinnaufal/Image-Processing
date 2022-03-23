import cv2

import numpy as np

#membaca citra digital dari komputer
citra = cv2.imread("D:\Citra\LOGO UNIB.png")

#membaca channel warna rgb jumlah piksel
b = citra[:,:,0]
g = citra[:,:,1]
r = citra[:,:,2]

#menyimpan jumlah baris dan kolom dari citra
jum_baris = len(citra)
jum_kolom = len(citra[0])

#menyiapkan citra baru dengan nilai 0
citra_gray = np.zeros((jum_baris, jum_kolom))

for i in range(jum_baris):
    for j in range(jum_kolom):
        citra_gray[i, j] = round(0.299 * r [i,j] + 0.587 * g [i,j] + 0.114 * b [i,j])

citra_gray = citra_gray.astype(np.uint8)

cv2.imshow("unib gray", citra_gray)

cv2.waitKey()