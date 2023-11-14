import cv2 as cv

"""img = cv.imread("photos/gojo.png")

cv.imshow("draw", img)
cv.waitKey(0)
"""

capture = cv.VideoCapture("videos/OpenCV Course - Full Tutorial with Python.mp4")

while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)

    if cv.waitKey(0) & 0xFF == ord("d"):
        break

capture.release()
cv.destroyAllWindows()
