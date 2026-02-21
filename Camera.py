# importing OpenCV library for image processing
import cv2

# importing the YOLO class from the ultralytics library for object detection
from ultralytics import YOLO


# Function to perform real-time object detection using the YOLO model and display the annotated video feed
def camera():

    # creating an instance of the YOLO model using the custom-trained weights from "best.pt"
    model = YOLO('best.pt')

    # opening the default camera (webcam) for video capture
    cap = cv2.VideoCapture(0)

    # continuously read frames from the camera and perform object detection until the camera is closed
    while cap.isOpened():

        # read a frame from the camera
        ret, frame = cap.read()

        # if the frame was not read successfully, break the loop
        if not ret:
            break

        # perform object detection on the current frame using the YOLO model with a confidence threshold of 0.6
        results = model(frame, conf=0.6)

        # plot the results on the frame to create an annotated frame with detected objects highlighted
        annotated_frame = results[0].plot()

        # resize the annotated frame to a specific size (800x500) and display it in a window titled "YOLOv8 Detection"
        x = cv2.resize(annotated_frame, (800, 500))

        # display the annotated frame in a window titled "Frame"
        cv2.imshow("Frame", x)

        # check if the 'q' key is pressed to break the loop and exit the video feed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # release the video capture object and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
