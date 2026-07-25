import cv2

# Read the image
img = cv2.imread(r"C:\Users\jerin\OneDrive\Pictures\Saved Pictures\Gojo jjk0 eyes.jpg")

# Check whether image is loaded
if img is None:
    print("Error: Image not found!")
else:
    # Apply Gaussian Blur
    blur = cv2.GaussianBlur(img, (31,31), 0)

    # Resize images (optional, for large images)
    img = cv2.resize(img, (800,600))
    blur = cv2.resize(blur, (800,600))

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Blurred Image", blur)

    # Wait for key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
