# Stone-detection
# Environment
     Python = 3.6.12
     Numpy = 1.18.5
     Opencv-python = 4.1.2.30
# Data
       ./video.avi
# Test
       python dealWithVideo.py
# Result
       ./video_new.avi
# The interpretation of dealWithVideo.py 
## 1.Because of the lighting conditions, the detection effect of places with poor lighting contrast is not ideal, so first cut each frame of the video, carry out binary detection respectively.
### crop & binary detection

#### Left
![three](https://user-images.githubusercontent.com/78291941/131469538-37c4d250-1fff-4f2b-975b-a3bbfc5bcdb5.jpg) 
#### Right
![two](https://user-images.githubusercontent.com/78291941/131470718-c1188ec1-d71f-462c-9fc0-53179daf4974.jpg)
## 2.Connect the cropped and binarized images
![1](https://user-images.githubusercontent.com/78291941/131470780-20fd266f-0524-4f21-b722-29bd87f86560.jpg)
## 3.Edge detection
![2](https://user-images.githubusercontent.com/78291941/131471634-9937d7a5-4edf-4a71-9f17-a3504539afbc.jpg)
## 4.Overlay the edge detection results with the original image
![hello](https://user-images.githubusercontent.com/78291941/131472003-ad088807-c62f-44c4-b58a-bf979a4e76cc.jpg)
