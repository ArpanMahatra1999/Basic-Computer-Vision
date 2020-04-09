import cv2

# for colored image use 1
imgColored = cv2.imread("duck.jpg", 1)
print(imgColored)
print(type(imgColored))
print(imgColored.shape)

# for grayscale image use 0
imgGrayscale = cv2.imread("duck.jpg", 0)
print(imgGrayscale)
print(type(imgGrayscale))
print(imgGrayscale.shape)
