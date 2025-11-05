import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

def load_image():
    path = "images/trex.png"
    if not os.path.exists(path):
        raise FileNotFoundError("Gambar tidak ditemukan!")
    return cv2.imread(path)

def resize_for_display(image, max_width=400):
    (h, w) = image.shape[:2]
    if w > max_width:
        r = max_width / w
        image = cv2.resize(image, (max_width, int(h * r)))
    return image

def main():
    image = resize_for_display(load_image())

    chans = cv2.split(image)
    colors = ("b", "g", "r")

    fig = plt.figure("2D Color Histogram")
    plt.title("Histogram 2D antara Green dan Red Channel")
    hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])

    plt.imshow(hist, interpolation="nearest")
    plt.xlabel("Red")
    plt.ylabel("Green")
    plt.colorbar()
    plt.show()

if __name__ == "__main__":
    main()
