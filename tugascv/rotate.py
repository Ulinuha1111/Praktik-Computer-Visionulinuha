import cv2
import numpy as np
import os

def load_image():
    path = "images/trex.png"
    if not os.path.exists(path):
        raise FileNotFoundError(f"Gambar tidak ditemukan: {path}")
    return cv2.imread(path)

def rotate(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(image, M, (w, h))

def resize_for_display(image, max_width=500):
    """Perkecil gambar agar tampilan tidak terlalu besar di layar"""
    (h, w) = image.shape[:2]
    if w > max_width:
        ratio = max_width / w
        image = cv2.resize(image, (max_width, int(h * ratio)))
    return image

def main():
    image = load_image()
    image = resize_for_display(image)  # 🔹 perkecil sebelum ditampilkan

    cv2.imshow("Original", image)

    rotated45 = rotate(image, 45)
    rotated45 = resize_for_display(rotated45)
    cv2.imshow("Rotated 45°", rotated45)
    cv2.waitKey(0)

    rotated90 = rotate(image, -90)
    rotated90 = resize_for_display(rotated90)
    cv2.imshow("Rotated -90°", rotated90)
    cv2.waitKey(0)

    rotated180 = rotate(image, 180)
    rotated180 = resize_for_display(rotated180)
    cv2.imshow("Rotated 180°", rotated180)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
