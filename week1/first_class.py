import cv2

image_path = "/Users/aakarshankhadka/Documents/ComputerVisionIslington/week1/image.png"
img = cv2.imread(image_path)

cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
