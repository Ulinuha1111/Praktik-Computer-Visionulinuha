import cv2
import numpy as np
import os

def load_image():
    """Muat gambar utama dari folder images"""
    path = "images/trex.png"
    if not os.path.exists(path):
        raise FileNotFoundError(f"Gambar tidak ditemukan: {path}")
    return cv2.imread(path)

def resize_for_display(image, max_width=500):
    """Perkecil gambar agar tidak terlalu besar saat ditampilkan"""
    (h, w) = image.shape[:2]
    if w > max_width:
        ratio = max_width / w
        image = cv2.resize(image, (max_width, int(h * ratio)))
    return image

def main():
    image = load_image()
    image = resize_for_display(image)
    cv2.imshow("Original", image)

    # Buat mask lingkaran
    mask = np.zeros(image.shape[:2], dtype="uint8")
    center_x, center_y = image.shape[1] // 2, image.shape[0] // 2
    radius = min(center_x, center_y) // 2
    cv2.circle(mask, (center_x, center_y), radius, 255, -1)

    cv2.imshow("Mask (Lingkaran)", mask)
    cv2.waitKey(0)

    # Terapkan mask ke gambar (bitwise AND)
    masked = cv2.bitwise_and(image, image, mask=mask)
    masked = resize_for_display(masked)
    cv2.imshow("Masked Result", masked)
    cv2.waitKey(0)

    # Contoh tambahan: persegi untuk banding
    rect_mask = np.zeros(image.shape[:2], dtype="uint8")
    cv2.rectangle(rect_mask, (center_x - radius, center_y - radius),
                  (center_x + radius, center_y + radius), 255, -1)
    rect_masked = cv2.bitwise_and(image, image, mask=rect_mask)
    rect_masked = resize_for_display(rect_masked)
    cv2.imshow("Rectangular Masked Result", rect_masked)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
