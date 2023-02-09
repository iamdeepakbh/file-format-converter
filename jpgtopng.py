import cv2

# Load the image
img = cv2.imread("image.jpg")

# Save the image in a different format
cv2.imwrite("image.png", img)
