import cv2

img = cv2.imread(r"C:\Users\jerin\OneDrive\Pictures\Saved Pictures\tree.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Resize both images
img = cv2.resize(img, (800, 600))
gray = cv2.resize(gray, (800, 600))

cv2.imshow("Original", img)
cv2.imshow("Gray", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
