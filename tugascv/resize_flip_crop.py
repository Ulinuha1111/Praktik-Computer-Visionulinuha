import cv2
import os

def load_image():
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

    (h, w) = image.shape[:2]

    # resize by width
    resized_w = cv2.resize(image, (200, int(h * 200 / w)))
    cv2.imshow("Resized width=200", resized_w)
    cv2.waitKey(0)

    # resize by height
    resized_h = cv2.resize(image, (int(w * 150 / h), 150))
    cv2.imshow("Resized height=150", resized_h)
    cv2.waitKey(0)

    # flip horizontal
    flipped_h = cv2.flip(image, 1)
    cv2.imshow("Flipped Horizontal", flipped_h)
    cv2.waitKey(0)

    # flip vertical
    flipped_v = cv2.flip(image, 0)
    cv2.imshow("Flipped Vertical", flipped_v)
    cv2.waitKey(0)

    # flip both
    flipped_b = cv2.flip(image, -1)
    cv2.imshow("Flipped Both", flipped_b)
    cv2.waitKey(0)

    # crop center
    startX, startY = w // 4, h // 4
    crop = image[startY:startY + h // 2, startX:startX + w // 2]
    cv2.imshow("Cropped Center", crop)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
