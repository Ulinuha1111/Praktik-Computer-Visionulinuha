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
    """Perkecil gambar agar tampil nyaman di layar"""
    (h, w) = image.shape[:2]
    if w > max_width:
        ratio = max_width / w
        image = cv2.resize(image, (max_width, int(h * ratio)))
    return image

def main():
    # 1️⃣ Muat dan tampilkan gambar asli
    image = load_image()
    image = resize_for_display(image)
    cv2.imshow("Original", image)

    # 2️⃣ Pisahkan channel warna (B, G, R)
    (B, G, R) = cv2.split(image)

    cv2.imshow("Blue Channel", B)
    cv2.imshow("Green Channel", G)
    cv2.imshow("Red Channel", R)
    cv2.waitKey(0)

    # 3️⃣ Gabungkan kembali channel menjadi gambar penuh
    merged = cv2.merge([B, G, R])
    merged = resize_for_display(merged)
    cv2.imshow("Merged Channels", merged)
    cv2.waitKey(0)

    # 4️⃣ Contoh tambahan — tampilkan warna dominan tiap channel
    zeros = np.zeros(image.shape[:2], dtype="uint8")
    cv2.imshow("Blue Only", cv2.merge([B, zeros, zeros]))
    cv2.imshow("Green Only", cv2.merge([zeros, G, zeros]))
    cv2.imshow("Red Only", cv2.merge([zeros, zeros, R]))
    cv2.waitKey(0)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
