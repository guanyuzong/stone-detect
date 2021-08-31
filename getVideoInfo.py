# -*- coding: UTF-8 -*-
import cv2


def get_source_info_opencv(source_name):
    return_value = 0
    try:
        cap = cv2.VideoCapture(source_name)
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        fps = cap.get(cv2.CAP_PROP_FPS)
        num_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        print("width:{} \nheight:{} \nfps:{} \nnum_frames:{}".format(width, height, fps, num_frames))
    except (OSError, TypeError, ValueError, KeyError, SyntaxError) as e:
        print("init_source:{} error. {}\n".format(source_name, str(e)))
        return_value = -1
    return return_value


def main():
    source_name = "video.avi"
    get_source_info_opencv(source_name)


if __name__ == "__main__":
    main()
