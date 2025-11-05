import cv2
import os

def load_image():
    path = "images/trex.png"
    if not os.path.exists(path):
        raise FileNotFoundError("Gambar tidak ditemukan: images/trex.png")
    return cv2.imread(path)

def resize_for_display(image, max_width=500):
    (h, w) = image.shape[:2]
    if w > max_width:
        r = max_width / w
        image = cv2.resize(image, (max_width, int(h * r)))
    return image

def main():
    image = resize_for_display(load_image())
    cv2.imshow("Original (BGR)", image)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    cv2.imshow("Grayscale", gray)
    cv2.imshow("HSV", hsv)
    cv2.imshow("LAB", lab)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
