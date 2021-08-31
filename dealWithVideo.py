# -*- coding: utf-8 -*-
import cv2

import numpy as np
import logging


def crop(img):       # 因为光照条件，光照条件较差的地方其检测效果不好，所以先进性裁剪，分别检测后，再进行合并
    xy = cv2.flip(img, -1)
    crop_img0 = img[0:1000, 400:1000]
    crop_img1 = xy[0:1000, 600:1000]
    crop_img1 = cv2.flip(crop_img1, -1)
    return crop_img0,crop_img1

def thred(image):    #二值化
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    ret1, two = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY_INV)
    return two

def thred1(image):   #二值化
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    ret1, two = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV)
    return two
'''
thred,thred1阈值度均可自行调节
'''
def demo(image1,image2): #与原图进行覆盖

    img2 = cv2.imread(image2)
    alpha = 1
    meta =  2
    gamma = 0
    image = cv2.addWeighted(image1, alpha, img2, meta, gamma)
    return image



file_path = 'video.avi'

vc = cv2.VideoCapture(file_path)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps =vc.get(cv2.CAP_PROP_FPS)
size = (int(vc.get(cv2.CAP_PROP_FRAME_WIDTH)), int(vc.get(cv2.CAP_PROP_FRAME_HEIGHT)))
out = cv2.VideoWriter("D:/video/video_new1.avi",fourcc, fps, size)

while(vc.isOpened()):
    ret, frame = vc.read()
    if ret==True:
        b, g, r = cv2.split(frame)
        img_rgb = cv2.merge([r, g, b])

        path1, path2 = crop(img_rgb)  # 裁剪

        step1 = thred(path1)  # 二值化后合并 二值化的阈值根据不同的条件自行设置
        step2 = thred1(path2)
        path3 = np.hstack([step2, step1])
        cv2.imwrite('./1.jpg', path3)

        img = cv2.imread("./1.jpg")
        blurred = cv2.GaussianBlur(img, (1, 1), 10)
        out_img_GRAY = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)  # 将图片转换为灰度图

        laplacian = cv2.Laplacian(out_img_GRAY, -1)  # 边缘检测算子进行检测
        cv2.imwrite('./2.jpg', laplacian)

        final = demo(img_rgb, './2.jpg')  # 将检测后的图像与原图进行覆盖
        # save_image(count, final)
        cv2.imshow('1', out_img_GRAY)  # 将灰度效果和最终覆盖效果分别显示
        cv2.imshow('hello', final)

        out.write(final)     #将实验结果写入新的视频中去

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

vc.release()
out.release()
cv2.destroyAllWindows()

