import cv2
import numpy as np
import os

def load_image():
    path = "images/trex.png"
    if not os.path.exists(path):
        raise FileNotFoundError(f"Gambar tidak ditemukan: {path}")
    return cv2.imread(path)

def resize_for_display(image, max_width=500):
    """Perkecil gambar agar tidak terlalu besar di layar"""
    (h, w) = image.shape[:2]
    if w > max_width:
        ratio = max_width / w
        image = cv2.resize(image, (max_width, int(h * ratio)))
    return image

def main():
    image = load_image()
    image = resize_for_display(image)
    cv2.imshow("Original", image)

    # Buat matriks konstan untuk operasi aritmatika (menambah/kurangi brightness)
    M = np.full(image.shape, 50, dtype="uint8")

    # Tambahkan kecerahan
    added = cv2.add(image, M)
    added = resize_for_display(added)
    cv2.imshow("Added Brightness (+50)", added)
    cv2.waitKey(0)

    # Kurangi kecerahan
    sub = cv2.subtract(image, M)
    sub = resize_for_display(sub)
    cv2.imshow("Subtracted Brightness (-50)", sub)
    cv2.waitKey(0)

    # Gabungkan dua gambar (blending)
    blended = cv2.addWeighted(image, 0.7, M, 0.3, 0)
    blended = resize_for_display(blended)
    cv2.imshow("Blended (Weighted)", blended)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
