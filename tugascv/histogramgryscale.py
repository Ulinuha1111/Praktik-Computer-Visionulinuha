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
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale", gray)

    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

    plt.figure("Grayscale Histogram")
    plt.title("Histogram Grayscale")
    plt.xlabel("Intensitas")
    plt.ylabel("Jumlah Piksel")
    plt.plot(hist, color='black')
    plt.xlim([0, 256])
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
