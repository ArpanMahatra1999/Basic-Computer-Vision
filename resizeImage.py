import cv2

img = cv2.imread("duck.jpg", 0)
# resize_img = cv2.resize(img, (650, 500))
resize_img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Duck", resize_img)

# Wait for pressing key to close window
# cv2.waitKey(0)

# Wait for 3000 milliseconds to close window
cv2.waitKey(3000)

cv2.destroyAllWindows()
