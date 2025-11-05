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
    cv2.imshow("Original", image)

    # blur rata
    avg = cv2.blur(image, (7, 7))
    cv2.imshow("Average Blur (7x7)", avg)

    # gaussian blur
    gauss = cv2.GaussianBlur(image, (7, 7), 0)
    cv2.imshow("Gaussian Blur (7x7)", gauss)

    # median blur
    median = cv2.medianBlur(image, 7)
    cv2.imshow("Median Blur (7x7)", median)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
