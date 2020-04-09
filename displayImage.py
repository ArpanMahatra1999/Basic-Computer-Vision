import cv2

img = cv2.imread("duck.jpg", 0)
cv2.imshow("Duck", img)

# Wait for pressing key to close window
# cv2.waitKey(0)

# Wait for 3000 milliseconds to close window
cv2.waitKey(3000)

cv2.destroyAllWindows()
