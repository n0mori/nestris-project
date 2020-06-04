import numpy as np
import cv2 as cv

BLACK = np.array([0, 0, 0])

def process_block(img, i0, j0):
    if img[i0,j0] == BLACK:
        return (False, None, None)

    colors = (img[i0,j0], img[i0, j0 + 1])
    filled = img[i0 + 2, j0 + 2] == colors[0]
    return True, colors, filled


def main():
    img = cv.imread('frame.png')
    mat = np.zeros((20, 10, 3))
    data = (None * 10) * 20

    # for i in range(40, 198, 9):
    #     for j in range(96, 174, 9):

    for i in range(20):
        for j in range(10):
            pixel = img[40 + 8 * i, 96 + 8 * j]        
            mat[i,j] = pixel
            # if :
            #     mat[i, j] = 1

    cv.imwrite('mat.png', mat)




if __name__ == "__main__":
    main()