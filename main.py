import numpy as np
import cv2 as cv

BLACK = [0, 0, 0]
img = cv.imread('frame.png')

mat = np.zeros((20, 10, 3))

# for i in range(40, 198, 9):
#     for j in range(96, 174, 9):

for i in range(20):
    for j in range(10):
        pixel = img[40 + 9 * i, 97 + 9 * j]        
        mat[i,j] = pixel
        # if :
        #     mat[i, j] = 1

cv.imwrite('mat.png', mat)
# print(mat)