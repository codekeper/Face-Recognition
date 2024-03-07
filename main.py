import cv2

if __name__ == '__main__':

    # Load the Haar cascade classifier for frontal face detection:
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    if face_cascade.empty():
        print("Error: Cascade Classifier not loaded.")
        exit()

    # Open the camera:
    video_capture = cv2.VideoCapture(0)

    # check for the video captured object to open successfully:
    if not video_capture.isOpened():
        print("Error: Couldn't open the webcam.")
        exit()

    # Loop for capturing frames continuously(video):
    while True:
        ret, frame = video_capture.read()

        # Convert frame to grayscale (Haar cascade works in grayscale):
        grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame:
        faces = face_cascade.detectMultiScale(grayscale, scaleFactor=1.1, minNeighbors=5)

        # Draw rectangles around detected faces:
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (40, 250, 159), 2)

        # flip the camera window:
        frame = cv2.flip(frame, 1)

        # showing the final output:
        cv2.imshow("Camera", frame)

        # condition to close camera:
        if cv2.waitKey(1) & 0xFF == ord('q') or cv2.waitKey(1) & 0xFF == ord('Q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
