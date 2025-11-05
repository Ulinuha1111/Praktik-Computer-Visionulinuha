import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

def load_image():
    path = "images/trex.png"
    if not os.path.exists(path):
        raise FileNotFoundError("Gambar tidak ditemukan!")
    return cv2.imread(path)

def resize_for_display(image, max_width=500):
    (h, w) = image.shape[:2]
    if w > max_width:
        r = max_width / w
        image = cv2.resize(image, (max_width, int(h * r)))
    return image

def main():
    image = resize_for_display(load_image())
    cv2.imshow("Original", image)

    colors = ("b", "g", "r")
    plt.figure("Color Histogram")
    plt.title("Histogram Warna (BGR)")
    plt.xlabel("Intensitas")
    plt.ylabel("Jumlah Piksel")

    for (i, col) in enumerate(colors):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])

    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
