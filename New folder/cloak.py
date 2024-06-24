import streamlit as st
import cv2
import numpy as np
import time

def start_magic(color):
    print("""
    Harry :  Hey !! Would you like to try my invisibility cloak ??
            Its awesome !!
            Prepare to get invisible .....................
        """)

    print("Colors = green, blue, red, yellow, orange, white, human skin")
    # Initialize all color variables to 0
    green = blue = red = yellow = orange = white = black = 0

    cap = cv2.VideoCapture(0)
    time.sleep(3)
    background = None  # Initialize background to None
    img = 0

    for i in range(30):
        ret, background = cap.read()

    background = np.flip(background, axis=1)

    while cap.isOpened():
        ret, img = cap.read()

        if not ret:
            print("Failed to read frame from camera")
            break


        # Flipping the image (Can be uncommented if needed)
        img = np.flip(img, axis=1)

        # Converting image to HSV color space.
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # Value for blurring
        value = (35, 35)

        # Initialize masks to zeros
        mask1 = mask2 = np.zeros_like(hsv)

        # Condition for Choosing Color
        if color == 'red':
            # Defining lower range for red color detection.
            lower_red = np.array([0, 120, 70])
            upper_red = np.array([10, 255, 255])
            mask1 = cv2.inRange(hsv, lower_red, upper_red)

            # Defining upper range for red color detection
            lower_red = np.array([170, 120, 70])
            upper_red = np.array([180, 255, 255])
            mask2 = cv2.inRange(hsv, lower_red, upper_red)

        elif color == 'yellow':
            # Defining the first range for yellow color detection.
            lower_yellow = np.array([20, 100, 100])
            upper_yellow = np.array([30, 255, 255])
            mask1 = cv2.inRange(hsv, lower_yellow, upper_yellow)

            # Defining the second range for yellow color detection.
            lower_yellow = np.array([30, 100, 100])
            upper_yellow = np.array([40, 255, 255])
            mask2 = cv2.inRange(hsv, lower_yellow, upper_yellow)

        elif color == 'green':
            # Defining the first range for green color detection.
            lower_green = np.array([40, 40, 40])
            upper_green = np.array([80, 255, 255])
            mask1 = cv2.inRange(hsv, lower_green, upper_green)

            # Defining the second range for green color detection.
            lower_green = np.array([80, 40, 40])
            upper_green = np.array([120, 255, 255])
            mask2 = cv2.inRange(hsv, lower_green, upper_green)

        elif color == 'orange':
            # Defining the first range for orange color detection.
            lower_orange = np.array([0, 100, 100])
            upper_orange = np.array([20, 255, 255])
            mask1 = cv2.inRange(hsv, lower_orange, upper_orange)

            # Defining the second range for orange color detection.
            lower_orange = np.array([160, 100, 100])
            upper_orange = np.array([180, 255, 255])
            mask2 = cv2.inRange(hsv, lower_orange, upper_orange)

        elif color == 'blue':
            # Defining the first range for blue color detection.
            lower_blue = np.array([100, 50, 50])
            upper_blue = np.array([120, 255, 255])
            mask1 = cv2.inRange(hsv, lower_blue, upper_blue)

            # Defining the second range for blue color detection.
            lower_blue = np.array([210, 50, 50])
            upper_blue = np.array([240, 255, 255])
            mask2 = cv2.inRange(hsv, lower_blue, upper_blue)

        elif color == 'human skin':
            # Defining the first range for human skin color detection.
            lower_skin_1 = np.array([0, 20, 70])
            upper_skin_1 = np.array([20, 255, 255])
            mask1 = cv2.inRange(hsv, lower_skin_1, upper_skin_1)

            # Defining the second range for human skin color detection.
            lower_skin_2 = np.array([170, 20, 70])
            upper_skin_2 = np.array([180, 255, 255])
            mask2 = cv2.inRange(hsv, lower_skin_2, upper_skin_2)

        elif color == 'white':
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
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))

    cap.release()
    cv2.destroyAllWindows()

def main():
 
    st.write("Choose the Color: red, green, blue, yellow, orange, white, human skin")

    color = st.text_input('Enter the Color name:')
    
    if st.button('Start Magic', key='start_button'):
        start_magic(color)

if __name__ == "__main__":
    main()


#To run code use streamlit run C:\Users\ANANTH\Desktop\podaa\cloak.py