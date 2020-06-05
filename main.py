import numpy as np
import cv2 as cv

BLACK = np.array([0, 0, 0])

def process_block(img, i0, j0):
    if (img[i0, j0] == BLACK).all():
        return {'colored': False, 'colors': None, 'filled': None}

    colors = (img[i0,j0], img[i0, j0 + 1])
    filled = (img[i0 + 2, j0 + 2] == colors[0]).all()
    return {'colored': True, 'colors': colors, 'filled': filled}

def redraw(mat, block, i0, j0):
    if not block['colored']:
        return

    for i in range(7):
        for j in range(7):
            mat[i0 + i, j0 + j] = block['colors'][1]
    
    mat[i0, j0] = block['colors'][0]
    if block['filled']:
        for i in range(1,6):
            for j in range(1,6):
                mat[i0 + i, j0 + j] = block['colors'][0]
    else:
        mat[i0+1,j0+1] = block['colors'][0]
        mat[i0+2,j0+1] = block['colors'][0]
        mat[i0+1,j0+2] = block['colors'][0]


def main():
    img = cv.imread('frame.png')
    mat = np.zeros((20, 10, 3))
    reformed = np.zeros((20 * 8, 10 * 8, 3))
    data = np.empty((20,10), dtype=dict)

    # for i in range(40, 198, 9):
    #     for j in range(96, 174, 9):

    for i in range(20):
        for j in range(10):
            pixel = img[40 + 8 * i, 96 + 8 * j]        
            mat[i,j] = pixel
            data[i,j] = process_block(img, 40 + 8 * i, 96 + 8 * j)
        #     print(data[i][j]['colored'], end='')
        # print()

    # print(data)
    for i in range(20):
        for j in range(10):
            redraw(reformed, data[i,j], i * 8, j * 8)

    cv.imwrite('mat.png', mat)
    cv.imwrite('reformed.png', reformed)



if __name__ == "__main__":
    main()