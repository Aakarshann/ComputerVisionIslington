import cv2
import matplotlib.pyplot as plt

"""
pip install --no-cache-dir opencv-python
to install fresh from the internet ignoring cache.
"""

image_path_1 = "week3/image.png"
image_path_2 = "week3/rgb.png"
orignal_image = cv2.imread(image_path_2, cv2.COLOR_BGR2RGB)
gray_scale = cv2.cvtColor(orignal_image, cv2.COLOR_BGR2GRAY)
# orignal_image = cv2.imread(image_path_2, cv2.IMREAD_UNCHANGED)

sobel_x = cv2.Sobel(gray_scale, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray_scale, cv2.CV_64F, 0, 1, ksize=3)

sobel_x = cv2.Sobel(orignal_image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(orignal_image, cv2.CV_64F, 0, 1, ksize=3)

sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)
combined = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

orignal_image_shape = orignal_image.shape  # (4808, 3408, 3)
# (4808, 3408, 4) if image is read with cv2.IMREAD_UNCHANGED
print(
    "shape", orignal_image_shape, "\n", gray_scale.shape
)  #  (4808, 3408) for grayscale

cv2.namedWindow("Orignal Image", cv2.WINDOW_NORMAL)

# cv2.imshow("Orignal Image", orignal_image)
cv2.imshow("Orignal Image", gray_scale)

# Binarization
_, threshold = cv2.threshold(gray_scale, 127, 255, cv2.THRESH_BINARY_INV)
cv2.namedWindow("Threshold Image", cv2.WINDOW_NORMAL)
cv2.imshow("Threshold Image", threshold)

resized_image = cv2.resize(orignal_image, (300, 300))
cv2.namedWindow("Resized Image", cv2.WINDOW_NORMAL)
cv2.imshow("Resized Image", resized_image)

# plt.imshow("Orignal Image" , cv2.WINDOW_NORMAL)
# plt.title("Orignal (Possible BGR)")
# plt.show()

cv2.waitKey(0)
cv2.destroyWindow("Orignal Image")
