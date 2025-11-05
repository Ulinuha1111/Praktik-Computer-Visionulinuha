# getting_and_setting.py
import argparse
import cv2
import numpy as np
import os

def load_image(path=None):
    if path and os.path.exists(path):
        return cv2.imread(path)
    # fallback: create synthetic test image (350x228-like "trex")
    img = np.full((228, 350, 3), 254, dtype="uint8")
    cv2.putText(img, "TEST", (40,120), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,0), 3)
    return img

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=False, help="Path to image")
    args = vars(ap.parse_args())
    image = load_image(args.get("image"))
    cv2.imshow("Original", image)

    # access pixel (0,0)
    (b, g, r) = image[0, 0]
    print(f"Pixel at (0,0) - R: {r}, G: {g}, B: {b}")

    # set pixel (0,0) to red (remember OpenCV uses BGR)
    image[0, 0] = (0, 0, 255)
    (b, g, r) = image[0, 0]
    print(f"After set - Pixel at (0,0) - R: {r}, G: {g}, B: {b}")

    # crop top-left 100x100
    corner = image[0:100, 0:100]
    cv2.imshow("Corner", corner)

    # set that corner to green
    image[0:100, 0:100] = (0, 255, 0)
    cv2.imshow("Updated", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
