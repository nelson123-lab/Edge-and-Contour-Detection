import cv2

# Read in the image
img = cv2.imread('image.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply the Canny edge detection algorithm
edges = cv2.Canny(gray, 100, 200)

# Find the contours in the image
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw the contours on the original image
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

# Display the original image with contours
cv2.imshow('Image with Contours', img)

# Display the edge-detected image
cv2.imshow('Edges', edges)

# Wait for a key press and then exit
cv2.waitKey(0)
cv2.destroyAllWindows()
