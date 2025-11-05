# drawing.py
import numpy as np
import cv2

def main():
    # canvas 300x300
    canvas = np.zeros((300, 300, 3), dtype="uint8")

    green = (0, 255, 0)
    cv2.line(canvas, (0, 0), (300, 300), green)
    cv2.imshow("Line1", canvas)
    cv2.waitKey(0)

    red = (0, 0, 255)
    cv2.line(canvas, (300, 0), (0, 300), red, 3)
    cv2.imshow("Line2", canvas)
    cv2.waitKey(0)

    # rectangles
    cv2.rectangle(canvas, (10, 10), (60, 60), green)
    cv2.imshow("Rect1", canvas)
    cv2.waitKey(0)

    cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
    cv2.imshow("Rect2", canvas)
    cv2.waitKey(0)

    blue = (255, 0, 0)
    cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)  # filled
    cv2.imshow("RectFilled", canvas)
    cv2.waitKey(0)

    # draw concentric circles
    canvas = np.zeros((300, 300, 3), dtype="uint8")
    (centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
    white = (255, 255, 255)
    for r in range(0, 175, 25):
        cv2.circle(canvas, (centerX, centerY), r, white)
    cv2.imshow("Concentric", canvas)
    cv2.waitKey(0)

    # random circles
    for i in range(0, 25):
        radius = np.random.randint(5, high=200)
        color = np.random.randint(0, high=256, size=(3,)).tolist()
        pt = np.random.randint(0, high=300, size=(2,))
        cv2.circle(canvas, tuple(pt), int(radius), color, -1)
    cv2.imshow("Random Circles", canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
