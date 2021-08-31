import numpy as np
import cv2
def func2(path1,path2):
    # path1 = 'D:/4.jpg'
    # path2 = 'D:/44.jpg'
    img1 = cv2.imread(path1)
    img2 = cv2.imread(path2)
    img3 = np.hstack([img1, img2])
    cv2.imshow('img3',img3)
    cv2.waitKey()
if __name__ == '__main__':
    path1 = 'D:/44.jpg'
    path2 = 'D:/4.jpg'
    func2(path1,path2)