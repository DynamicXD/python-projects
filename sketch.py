import cv2
image = cv2.imread("C:/Users/USER/Downloads/mrbot.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted = 255-gray_image
blur = cv2.GaussianBlur(inverted, (21, 21), 0)
invertedblur = 255-blur
sketch = cv2.divide(gray_image, invertedblur, scale=256.0)
cv2.imwrite("sketch.png", sketch)
cv2.imshow("Image", sketch)
