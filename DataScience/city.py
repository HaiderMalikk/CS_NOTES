# Install OpenCV if needed
import cv2
import numpy as np
import matplotlib.pyplot as plt
from urllib.request import urlopen
import os

# Download a sample image
image_path = 'city.jpg'

# Read the image
img = cv2.imread(image_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 1. Harris Corner Detection
gray_float = np.float32(gray)
corners = cv2.cornerHarris(gray_float, blockSize=2, ksize=3, k=0.04)
# Dilate to mark the corners
corners = cv2.dilate(corners, None)
# Create a copy of the original image
img_harris = img.copy()
# Mark corners with red color (threshold for best corners)
img_harris[corners > 0.01 * corners.max()] = [0, 0, 255]

# 2. Shi-Tomasi Corner Detection
corners_st = cv2.goodFeaturesToTrack(gray, maxCorners=50, qualityLevel=0.01, minDistance=10)
img_shi_tomasi = img.copy()
# Draw circles around detected corners
if corners_st is not None:
    for corner in corners_st:
        x, y = corner.ravel()
        cv2.circle(img_shi_tomasi, (int(x), int(y)), 5, (0, 255, 0), -1)

# 3. SIFT (Scale-Invariant Feature Transform)
sift = cv2.SIFT_create()
keypoints_sift = sift.detect(gray, None)
img_sift = cv2.drawKeypoints(img, keypoints_sift, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# 4. ORB (Oriented FAST and Rotated BRIEF)
orb = cv2.ORB_create(nfeatures=200)
keypoints_orb = orb.detect(gray, None)
img_orb = cv2.drawKeypoints(img, keypoints_orb, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# 5. Canny Edge Detection
edges = cv2.Canny(gray, 100, 200)


# 6. Sobel Edge Detection
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)  # x direction
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)  # y direction
sobel_combined = cv2.magnitude(sobelx, sobely)
# Normalize to 0-255 for visualization
sobel_combined = np.uint8(255 * sobel_combined / np.max(sobel_combined))

# 7. Hough Line Transform
edges_for_hough = cv2.Canny(gray, 50, 150, apertureSize=3)
img_hough = img.copy()
lines = cv2.HoughLines(edges_for_hough, 1, np.pi/180, threshold=150)
if lines is not None:
    for line in lines[:15]:  # Limit to 15 lines for clarity
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(img_hough, (x1, y1), (x2, y2), (0, 0, 255), 2)

# 8. Contour Detection
_, thresh = cv2.threshold(gray, 127, 255, 0)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img_contours = img.copy()
cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 2)

# 9. Watershed Segmentation
# Use distance transform to segment touching objects
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# Noise removal
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# Sure background area
sure_bg = cv2.dilate(opening, kernel, iterations=3)
# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)
sure_fg = np.uint8(sure_fg)
# Finding unknown region
unknown = cv2.subtract(sure_bg, sure_fg)
# Marker labeling
ret, markers = cv2.connectedComponents(sure_fg)
# Add 1 to all labels so that background is not 0, but 1
markers = markers + 1
# Mark unknown region with 0
markers[unknown == 255] = 0
# Apply watershed
img_watershed = img.copy()
markers = cv2.watershed(img_watershed, markers)
img_watershed[markers == -1] = [0, 0, 255]  # Mark watershed boundaries in red

# 10. Gabor Filter for Texture Analysis
# Create a bank of Gabor filters
g_kernel = cv2.getGaborKernel((21, 21), 5, 1, 10, 1, 0, ktype=cv2.CV_32F)
g_kernel /= g_kernel.sum()
img_gabor = cv2.filter2D(gray, cv2.CV_8UC3, g_kernel)

# 11. HOG (Histogram of Oriented Gradients) Visualization
# Resize image to match HOG descriptor's expected window size
img_resized = cv2.resize(img, (64, 128))
gray_resized = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
# HOG parameters
win_size = (64, 128)
block_size = (16, 16)
block_stride = (8, 8)
cell_size = (8, 8)
nbins = 9
# Create HOG descriptor
hog = cv2.HOGDescriptor(win_size, block_size, block_stride, cell_size, nbins)
# Compute HOG features
hog_features = hog.compute(gray_resized)  # Use the grayscale image for HOG computation
# For visualization, we'll use a simple approach: draw cells and gradients
img_hog = img_resized.copy()
cell_size_x, cell_size_y = cell_size
for y in range(0, img_hog.shape[0], cell_size_y):
    for x in range(0, img_hog.shape[1], cell_size_x):
        cv2.rectangle(img_hog, (x, y), (x + cell_size_x, y + cell_size_y), (0, 255, 0), 1)

# Additional CV techniques beyond the original 12

# 13. Laplacian Edge Detection
laplacian = cv2.Laplacian(gray, cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))

# 14. Bilateral Filter (Edge-preserving smoothing)
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

# 15. Median Blur (Noise reduction)
median_blur = cv2.medianBlur(img, 5)

# 16. Adaptive Thresholding
adaptive_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                        cv2.THRESH_BINARY, 11, 2)

# 17. Posterize effect (color quantization)
z = img.reshape((-1, 3))
z = np.float32(z)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 8  # Number of colors
ret, label, center = cv2.kmeans(z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
center = np.uint8(center)
res = center[label.flatten()]
posterized = res.reshape((img.shape))

# 18. Emboss effect 
kernel_emboss = np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]])
emboss = cv2.filter2D(gray, -1, kernel_emboss)
emboss = cv2.cvtColor(emboss, cv2.COLOR_GRAY2BGR)
emboss = cv2.add(emboss, np.array([128, 128, 128], dtype=np.uint8))

# 19. Pencil sketch effect
img_gray, img_sketch = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
# Note: img_sketch is already in BGR format, no need to convert

# 20. Stylization effect (Cartoonize)
stylization = cv2.stylization(img, sigma_s=60, sigma_r=0.07)

# 21. Detail Enhancement
detail = cv2.detailEnhance(img, sigma_s=10, sigma_r=0.15)

# 22. Cartoon effect
# First step: Edge detection
gray_cartoon = cv2.medianBlur(gray, 5)
edges_cartoon = cv2.Laplacian(gray_cartoon, cv2.CV_8U, ksize=5)
ret, mask = cv2.threshold(edges_cartoon, 100, 255, cv2.THRESH_BINARY_INV)
# Second step: Color quantization
cartoon = cv2.bilateralFilter(img, 9, 300, 300)
# Combine edges and color
cartoon = cv2.bitwise_and(cartoon, cartoon, mask=mask)

# 23. Solarize effect (invert colors above threshold)
solarized = img.copy()
thresh = 100
solarized[img > thresh] = 255 - solarized[img > thresh]

# 24. Prewitt edge detection (similar to Sobel but different kernels)
kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
prewitt_x = cv2.filter2D(gray, -1, kernelx)
prewitt_y = cv2.filter2D(gray, -1, kernely)
prewitt = cv2.addWeighted(prewitt_x, 0.5, prewitt_y, 0.5, 0)

# Convert BGR to RGB for matplotlib display
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_harris_rgb = cv2.cvtColor(img_harris, cv2.COLOR_BGR2RGB)
img_shi_tomasi_rgb = cv2.cvtColor(img_shi_tomasi, cv2.COLOR_BGR2RGB)
img_sift_rgb = cv2.cvtColor(img_sift, cv2.COLOR_BGR2RGB)
img_orb_rgb = cv2.cvtColor(img_orb, cv2.COLOR_BGR2RGB)
img_hough_rgb = cv2.cvtColor(img_hough, cv2.COLOR_BGR2RGB)
img_contours_rgb = cv2.cvtColor(img_contours, cv2.COLOR_BGR2RGB)
img_watershed_rgb = cv2.cvtColor(img_watershed, cv2.COLOR_BGR2RGB)
img_hog_rgb = cv2.cvtColor(img_hog, cv2.COLOR_BGR2RGB)

# Create a directory to save the processed images
output_dir = "CV_city"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Created directory: {output_dir}")

# Save all the processed images in a visually appealing order for the GIF
cv2.imwrite(os.path.join(output_dir, "01_original.jpg"), img)
cv2.imwrite(os.path.join(output_dir, "02_bilateral_filter.jpg"), bilateral)  # Subtle smoothing effect
cv2.imwrite(os.path.join(output_dir, "03_detail_enhanced.jpg"), detail)  # Enhanced details
cv2.imwrite(os.path.join(output_dir, "04_median_blur.jpg"), median_blur)  # Noise reduction
cv2.imwrite(os.path.join(output_dir, "05_harris_corners.jpg"), img_harris)  # Beginning of feature detection
cv2.imwrite(os.path.join(output_dir, "06_shi_tomasi.jpg"), img_shi_tomasi)  # Similar corner detection
cv2.imwrite(os.path.join(output_dir, "07_sift.jpg"), img_sift)  # Feature detection
cv2.imwrite(os.path.join(output_dir, "08_orb.jpg"), img_orb)  # More features

# Move to edge detection - progressively more defined edges
cv2.imwrite(os.path.join(output_dir, "09_sobel_edges.jpg"), cv2.cvtColor(sobel_combined, cv2.COLOR_GRAY2BGR))
cv2.imwrite(os.path.join(output_dir, "10_laplacian_edge.jpg"), cv2.cvtColor(laplacian, cv2.COLOR_GRAY2BGR))
cv2.imwrite(os.path.join(output_dir, "11_prewitt_edge.jpg"), cv2.cvtColor(prewitt, cv2.COLOR_GRAY2BGR))
cv2.imwrite(os.path.join(output_dir, "12_canny_edges.jpg"), cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR))

# Lines and shapes
cv2.imwrite(os.path.join(output_dir, "13_hough_lines.jpg"), img_hough)
cv2.imwrite(os.path.join(output_dir, "14_contours.jpg"), img_contours)
cv2.imwrite(os.path.join(output_dir, "15_watershed.jpg"), img_watershed)

# Texture and analysis
cv2.imwrite(os.path.join(output_dir, "16_gabor_filter.jpg"), cv2.cvtColor(img_gabor, cv2.COLOR_GRAY2BGR))
cv2.imwrite(os.path.join(output_dir, "17_hog.jpg"), img_hog)
cv2.imwrite(os.path.join(output_dir, "18_adaptive_threshold.jpg"), cv2.cvtColor(adaptive_thresh, cv2.COLOR_GRAY2BGR))

# # Artistic effects for dramatic finale
# cv2.imwrite(os.path.join(output_dir, "19_emboss.jpg"), emboss)
# cv2.imwrite(os.path.join(output_dir, "20_solarized.jpg"), solarized)
# cv2.imwrite(os.path.join(output_dir, "21_posterized.jpg"), posterized)
# cv2.imwrite(os.path.join(output_dir, "22_pencil_sketch.jpg"), img_sketch)
# cv2.imwrite(os.path.join(output_dir, "23_stylization.jpg"), stylization)
# cv2.imwrite(os.path.join(output_dir, "24_cartoon.jpg"), cartoon)

print(f"Saved all processed images in optimized order to {output_dir}/ (total: 24 images)")