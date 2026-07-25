import cv2
import numpy as np
import matplotlib.pyplot as plt

# ============================
# Load the image
# ============================

img = cv2.imread(r"C:\Users\jerin\OneDrive\Pictures\Saved Pictures\tree.jpg")

# Check whether image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Convert BGR to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# ============================
# Step 1: Simulate Low Light
# ============================

low_light = (img * 0.4).astype(np.uint8)

# ============================
# Step 2: Add Gaussian Noise
# ============================

noise = np.random.normal(0, 20, img.shape)

noisy = low_light + noise

# Keep pixel values between 0 and 255
noisy = np.clip(noisy, 0, 255).astype(np.uint8)

# ============================
# Step 3: Blur the Image
# ============================

blurred = cv2.GaussianBlur(noisy, (7,7), 2)

# ============================
# Step 4: Image Enhancement
# ============================

lab = cv2.cvtColor(blurred, cv2.COLOR_RGB2LAB)

l, a, b = cv2.split(lab)

clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))

l = clahe.apply(l)

enhanced = cv2.merge((l,a,b))

enhanced = cv2.cvtColor(enhanced, cv2.COLOR_LAB2RGB)

# ============================
# Display Results
# ============================

titles = [
    "Original Image",
    "Low Light Image",
    "Noisy Image",
    "Blurred Image",
    "Enhanced Image"
]

images = [
    img,
    low_light,
    noisy,
    blurred,
    enhanced
]

plt.figure(figsize=(18,5))

for i in range(len(images)):
    plt.subplot(1,5,i+1)
    plt.imshow(images[i])
    plt.title(titles[i], fontsize=10)
    plt.axis("off")

plt.tight_layout()

plt.show()
