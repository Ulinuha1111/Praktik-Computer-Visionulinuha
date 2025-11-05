import cv2
import numpy as np

def resize_for_display(image, max_width=400):
    """Perkecil hasil agar tampil nyaman di layar"""
    (h, w) = image.shape[:2]
    if w > max_width:
        ratio = max_width / w
        image = cv2.resize(image, (max_width, int(h * ratio)))
    return image

def main():
    # buat gambar hitam ukuran 300x300
    rectangle = np.zeros((300, 300), dtype="uint8")
    circle = np.zeros((300, 300), dtype="uint8")

    # gambar persegi putih dan lingkaran putih
    cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
    cv2.circle(circle, (150, 150), 150, 255, -1)

    # operasi bitwise
    bitwiseAnd = cv2.bitwise_and(rectangle, circle)
    bitwiseOr = cv2.bitwise_or(rectangle, circle)
    bitwiseXor = cv2.bitwise_xor(rectangle, circle)
    bitwiseNot = cv2.bitwise_not(circle)

    # perkecil tampilan agar pas di layar
    rectangle = resize_for_display(rectangle)
    circle = resize_for_display(circle)
    bitwiseAnd = resize_for_display(bitwiseAnd)
    bitwiseOr = resize_for_display(bitwiseOr)
    bitwiseXor = resize_for_display(bitwiseXor)
    bitwiseNot = resize_for_display(bitwiseNot)

    # tampilkan hasil
    cv2.imshow("Rectangle", rectangle)
    cv2.imshow("Circle", circle)
    cv2.imshow("AND", bitwiseAnd)
    cv2.imshow("OR", bitwiseOr)
    cv2.imshow("XOR", bitwiseXor)
    cv2.imshow("NOT", bitwiseNot)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
