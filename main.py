import cv2

if __name__ == '__main__':

    video_capture = cv2.VideoCapture(0)
    if not video_capture.isOpened():
        print("Error: Couldn't open the webcam.")
        exit()

    while True:
        ret, frame = video_capture.read()
        cv2.imshow("Video", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
