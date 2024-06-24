import cv2
import time
import numpy as np
from tkinter import *
import tkinter.messagebox as mb

global Color

def invisible_cloak():
    print("Colors = green, blue, red, yellow, orange, white, human skin")
    
    Color = str(color.get())
    # Initialize all color variables to 0
    green = blue = red = yellow = orange = white = black = 0

    cap = cv2.VideoCapture(0)
    time.sleep(5)
    img = 0
    background = 0
     

    for i in range(60):
        ret, background = cap.read()
        if not ret:
            break

    background = np.flip(background, axis=1)

    while cap.isOpened():
        ret, img = cap.read()
        if not ret:
            break

        img = np.flip(img, axis=1)

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        if Color == 'red':
            # Defining lower range for red color detection.
            lower_red = np.array([0, 120, 70])
            upper_red = np.array([10, 255, 255])
            mask1 = cv2.inRange(hsv, lower_red, upper_red)

            # Defining upper range for red color detection
            lower_red = np.array([170, 120, 70])
            upper_red = np.array([180, 255, 255])
            mask2 = cv2.inRange(hsv, lower_red, upper_red)

        elif Color == 'yellow':
            # Defining the first range for yellow color detection.
            lower_yellow = np.array([20, 100, 100])
            upper_yellow = np.array([30, 255, 255])
            mask1 = cv2.inRange(hsv, lower_yellow, upper_yellow)

            # Defining the second range for yellow color detection.
            lower_yellow = np.array([30, 100, 100])
            upper_yellow = np.array([40, 255, 255])
            mask2 = cv2.inRange(hsv, lower_yellow, upper_yellow)

        elif Color == 'green':
            # Defining the first range for green color detection.
            lower_green = np.array([40, 40, 40])
            upper_green = np.array([80, 255, 255])
            mask1 = cv2.inRange(hsv, lower_green, upper_green)

            # Defining the second range for green color detection.
            lower_green = np.array([80, 40, 40])
            upper_green = np.array([120, 255, 255])
            mask2 = cv2.inRange(hsv, lower_green, upper_green)

        elif Color == 'orange':
            # Defining the first range for orange color detection.
            lower_orange = np.array([0, 100, 100])
            upper_orange = np.array([20, 255, 255])
            mask1 = cv2.inRange(hsv, lower_orange, upper_orange)

            # Defining the second range for orange color detection.
            lower_orange = np.array([160, 100, 100])
            upper_orange = np.array([180, 255, 255])
            mask2 = cv2.inRange(hsv, lower_orange, upper_orange)

        elif Color == 'blue':
            # Defining the first range for blue color detection.
            lower_blue = np.array([100, 50, 50])
            upper_blue = np.array([120, 255, 255])
            mask1 = cv2.inRange(hsv, lower_blue, upper_blue)

            # Defining the second range for blue color detection.
            lower_blue = np.array([210, 50, 50])
            upper_blue = np.array([240, 255, 255])
            mask2 = cv2.inRange(hsv, lower_blue, upper_blue)

        elif Color == 'human skin':
            # Defining the first range for human skin color detection.
            lower_skin_1 = np.array([0, 20, 70])
            upper_skin_1 = np.array([20, 255, 255])
            mask1 = cv2.inRange(hsv, lower_skin_1, upper_skin_1)

            # Defining the second range for human skin color detection.
            lower_skin_2 = np.array([170, 20, 70])
            upper_skin_2 = np.array([180, 255, 255])
            mask2 = cv2.inRange(hsv, lower_skin_2, upper_skin_2)

        elif Color == 'white':
            lower_white = np.array([0, 0, 200])
            upper_white = np.array([180, 30, 255])
            mask1 = cv2.inRange(hsv, lower_white, upper_white)

            # Defining the second range for white color detection.
            lower_white = np.array([0, 0, 150])
            upper_white = np.array([180, 30, 200])
            mask2 = cv2.inRange(hsv, lower_white, upper_white)

        # ... (similar conditions for other colors)

        else:
            print("Choose the correct Color")
            break

        # Addition of the two masks to generate the final mask.
        mask = mask1 + mask2

        # Gaussian Blur
        mask_blur = cv2.GaussianBlur(mask1, (5, 5), 0)

        # Adaptive Thresholding
        _, mask_thresh = cv2.threshold(mask_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Contour Filtering
        contours, _ = cv2.findContours(mask_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            contour_area = [cv2.contourArea(c) for c in contours]
            max_contour_idx = np.argmax(contour_area)
            mask_filtered = np.zeros_like(mask_thresh)
            cv2.drawContours(mask_filtered, contours, max_contour_idx, (255, 255, 255), cv2.FILLED)
        else:
            mask_filtered = mask_thresh

        mask2 = cv2.bitwise_not(mask_filtered)

        res1 = cv2.bitwise_and(img, img, mask=mask2)
        res2 = cv2.bitwise_and(background, background, mask=mask_filtered)

        finalOutput = cv2.addWeighted(res1, 1, res2, 1, 0)
        cv2.imshow("Invisible Cloak", finalOutput)
        
        # Check for 'q' keypress to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Initializing the window
root = Tk()
root.title("Magic Cloak")
root.geometry("600x200")
root.resizable(0, 0)
root.config(bg='CadetBlue')

# Placing the components
Label(root, text='Harry Potter Invisible Cloak', font=("Comic Sans MS", 16, 'bold'), bg='CadetBlue').pack(side=TOP,fill=X)

Label(root, text='Choose the Color: red, green, blue, yellow, orange, white, human skin ', font=("Times New Roman", 14), bg='CadetBlue').place(x=20, y=50)

Label(root, text='Enter the Color name: ', font=("Times New Roman", 14), bg='CadetBlue').place(x=20, y=100)
color = StringVar()
Entry(root, width=40, textvariable=color, font=('Times New Roman', 14)).place(x=200, y=100)

Button(root, text='Start Magic', font=("Georgia", 10), width=15, command=invisible_cloak).place(x=220, y=150)

# Finalizing the window
root.update()
root.mainloop()
