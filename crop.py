import cv2
img = cv2.imread('D:/video/cutoutFromVideoResult/0.jpg')
#裁剪
xy = cv2.flip(img, -1)
crop_img = img[0:1000, 380:1000]
crop_img1 = xy[0:1000, 620:1000]
xy = cv2.flip(crop_img1, -1)
print(crop_img.shape)
# crop_img1 =img-crop_img
cv2.imwrite('D:/110.jpg', crop_img)
cv2.imwrite('D:/111.jpg', xy)
# cv2.imshow('crop_img1', crop_img1)
cv2.waitKey()

