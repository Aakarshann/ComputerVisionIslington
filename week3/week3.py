import cv2
import datetime
from datetime import datetime

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
print(f"{height}x{width} running at {fps}fps")

cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 500)

fourcc = cv2.VideoWriter_fourcc(*"XVID")  # Video writer for recording
out = cv2.VideoWriter(
    "output.mp4",
    fourcc,
    20.0,
    (width, height),
)

while True:
    ret, frame = cap.read()  # read the frame from the webcam

    if not ret:
        print("Error : Failed to capture frame")
        break

    frame = cv2.flip(frame, 1)  # horizantal flip
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    sobel_x = cv2.Sobel(gray_scale, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray_scale, cv2.CV_64F, 0, 1, ksize=3)
    sobel_x = cv2.convertScaleAbs(sobel_x)
    sobel_y = cv2.convertScaleAbs(sobel_y)
    combined = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)
    cv2.putText(
        frame, f"FPS: {fps}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2
    )
    cv2.putText(
        frame,
        f'Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}',
        (10, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2,
    )
    cv2.putText(
        frame,
        f"Resolution: {width}x{height}",
        (10, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2,
    )
    cv2.namedWindow("my webcam", cv2.WINDOW_NORMAL)
    cv2.imshow("my webcam", combined)
    out.write(combined)  # saving the output
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
