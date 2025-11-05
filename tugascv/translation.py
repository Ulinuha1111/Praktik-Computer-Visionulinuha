import cv2
import numpy as np
import os

def load_image():
    path = "images/trex.png"
    if not os.path.exists(path):
        raise FileNotFoundError(f"Gambar tidak ditemukan: {path}")
    return cv2.imread(path)

def translate(image, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

def main():
    image = load_image()

    max_width = 500
    (h, w) = image.shape[:2]
    if w > max_width:
        ratio = max_width / w
        image = cv2.resize(image, (max_width, int(h * ratio)))

    cv2.imshow("Original", image)

    shifted1 = translate(image, 25, 50)
    cv2.imshow("Shifted Down and Right", shifted1)
    cv2.waitKey(0)

    shifted2 = translate(image, -50, -90)
    cv2.imshow("Shifted Up and Left", shifted2)
    cv2.waitKey(0)

    shifted3 = translate(image, 0, 100)
    cv2.imshow("Shifted Down", shifted3)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
