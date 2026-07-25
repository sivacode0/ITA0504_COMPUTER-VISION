import cv2

# Read image
img = cv2.imread(r"C:\Users\jerin\OneDrive\Pictures\Saved Pictures\Awaken gojo satoru .png")

# Check image
if img is None:
    print("Error: Image not found!")
else:
    # Resize (optional)
    img = cv2.resize(img, (800,600))

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect edges
    edges = cv2.Canny(gray, 100, 200)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Grayscale Image", gray)
    cv2.imshow("Canny Edge Detection", edges)

    # Wait for key press
    cv2.waitKey(0)

    # Close windows
    cv2.destroyAllWindows()
