import cv2
import tkinter as tk
from PIL import Image, ImageTk

# Load the pre-trained Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the background image
bg_image = cv2.imread(r"C:/Users/ANANTH/Pictures/emoji4.png")

if bg_image is None:
    print("Error: Failed to load background image. Make sure the file path is correct.")
    exit()

# Print the dimensions of the background image
print("Background image dimensions:", bg_image.shape)

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        break

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # If no faces are detected, continue to the next frame
    if len(faces) == 0:
        continue

    # Get the dimensions of the first detected face
    (x, y, w, h) = faces[0]

    # Resize the background image to match the dimensions of the detected face
    bg_face = cv2.resize(bg_image, (w, h))

    # Replace the face region in the frame with the background face
    frame[y:y+h, x:x+w] = bg_face

    cv2.imshow("Frame", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()
