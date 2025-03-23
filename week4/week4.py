import cv2
import cv2.data

"""
https://github.com/opencv/opencv/tree/master/data/haarcascades
Above is the link to all of the models that OpenCV librarys under haarcascades detection concept.
We will use frontalface only.
"""

# Initializing the algorithm

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
image = cv2.imread("week4/image.png")
# image = cv2.imread("week4/image1.png")


# Haarcascades need gray scale images as an input.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.namedWindow("gray", cv2.WINDOW_NORMAL)
cv2.imshow("gray", gray)

# Initializing the built in face detection library
detected_faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.05,
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv2.CASCADE_SCALE_IMAGE,
)
print(detected_faces, "faces")  # [[133 123 135 135]]

# Drawing the rectangle around the face
for x, y, w, h in detected_faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.namedWindow("haarcascade face detection", cv2.WINDOW_NORMAL)
cv2.imshow("haarcascade face detection", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
