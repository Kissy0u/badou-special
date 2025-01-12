# author:牛欣明
# createTime: 2022年10月6日18:08:28
# describe: nearest neighbor interpolation最近邻插值
import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread("pic/lenna.png")
    h, w = img.shape[:2]
    scale = 2
    target_img = np.zeros((scale * h, scale * w, 3), np.float32)
    for i in range(scale * h):
        for j in range(scale * w):
            # for c in range(3):
            target_img[i, j] = img[int(i / scale), int(j / scale)]
    target_img = target_img.astype(np.uint8)
    cv2.imshow("target_img", target_img)
    cv2.imshow("src_img", img)
    cv2.waitKey()
