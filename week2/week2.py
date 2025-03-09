import cv2
import matplotlib.pyplot as plt

"""
pip install --no-cache-dir opencv-python
to install fresh from the internet ignoring cache.
"""

image_path_1 = "week1/image.png"
image_path_2 = "week2/rgb.png"
orignal_image = cv2.imread(image_path_2)
orignal_image = cv2.imread(image_path_2, cv2.IMREAD_UNCHANGED)


orignal_image_shape = orignal_image.shape  # (4808, 3408, 3)
# (4808, 3408, 4) if image is read with cv2.IMREAD_UNCHANGED
print("shape", orignal_image_shape)
cv2.namedWindow("Orignal Image", cv2.WINDOW_NORMAL)
cv2.imshow("Orignal Image", orignal_image)

cv2.waitKey(0)
cv2.destroyWindow("Orignal Image")
