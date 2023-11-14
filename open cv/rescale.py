import cv2 as cv

img = cv.imread("photos/gojo.png")

cv.imshow("draw", img)


cv.waitKey(0)
