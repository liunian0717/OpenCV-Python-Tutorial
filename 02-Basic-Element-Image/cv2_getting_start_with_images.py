import cv2

if __name__ == "__main__()":

    # 1.灰度图加载一张彩色图
    img = cv2.imread('lena.jpg', 0)


    # 2.显示图片
    cv2.imshow('02-Basic-Element-Image/lena', img)
    cv2.waitKey(0)

    # 先定义窗口，后显示图片
    cv2.namedWindow('lena2', cv2.WINDOW_NORMAL)
    cv2.imshow('lena2', img)
    cv2.waitKey(0)


    # 3.保存图片
    cv2.imwrite('lena_gray.jpg', img)

