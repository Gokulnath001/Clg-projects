import cv2
import numpy as np
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def replace_background(frame, bg_image, color):
    # Convert frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Convert color name to HSV range
    hsv_colors = {
        'red': ([0, 120, 70], [10, 255, 255], [170, 120, 70], [180, 255, 255]),
        'yellow': ([20, 100, 100], [30, 255, 255], [30, 100, 100], [40, 255, 255]),
        'green': ([40, 40, 40], [80, 255, 255], [80, 40, 40], [120, 255, 255]),
        'orange': ([0, 100, 100], [20, 255, 255], [160, 100, 100], [180, 255, 255]),
        'blue': ([100, 50, 50], [120, 255, 255], [210, 50, 50], [240, 255, 255]),
        'human skin': ([0, 20, 70], [20, 255, 255], [170, 20, 70], [180, 255, 255]),
        'white': ([0, 0, 200], [180, 30, 255], [0, 0, 150], [180, 30, 200]),
        'Purple': ([0,10,90],[210, 200, 230], [0,0,100], [250, 230, 255])
    }
    lower1, upper1, lower2, upper2 = hsv_colors[color]

    # Create masks for both color ranges
    mask1 = cv2.inRange(hsv, np.array(lower1), np.array(upper1))
    mask2 = cv2.inRange(hsv, np.array(lower2), np.array(upper2))

    # Combine masks
    mask = cv2.bitwise_or(mask1, mask2)

    # Invert the mask
    mask_inv = cv2.bitwise_not(mask)

    # Resize background image to match the frame size
    bg_image_resized = cv2.resize(bg_image, (frame.shape[1], frame.shape[0]))

    # Segregate the background and foreground based on masks
    bg = cv2.bitwise_and(bg_image_resized, bg_image_resized, mask=mask)
    fg = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Combine background and foreground
    result = cv2.add(bg, fg)

    return result

def start_magic():
    global cap
    color = color_entry.get()

    # Load the background image
    bg_image = cv2.imread(r"C:/Users/ANANTH/Pictures/beach.jpg")
    if bg_image is None:
        messagebox.showerror("Error", "Failed to load background image.")
        return

    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            messagebox.showerror("Error", "Failed to capture frame.")
            break

        frame = cv2.flip(frame, 1)  # Flip frame horizontally for mirror effect

        if color:
            frame = replace_background(frame, bg_image, color)

        # Display the frame
        cv2.imshow("Magic", frame)

        # Check for 'q' key to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Create a hover motion effect for buttons
def on_enter(event):
    start_button['background'] = 'light grey'

def on_leave(event):
    start_button['background'] = 'SystemButtonFace'

# Create the Tkinter window
root = tk.Tk()
root.title("Magic Background Replacement")
root.geometry("800x600")

# Set window background image
bg_image = Image.open(r"C:/Users/ANANTH/Pictures/beach.jpg")
bg_image = ImageTk.PhotoImage(bg_image)
background_label = tk.Label(root, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Label and Entry for color selection
color_label = tk.Label(root, text="Enter the Color name:", bg='light grey', font=('Arial', 14))
color_label.pack(pady=20)
color_entry = tk.Entry(root, font=('Arial', 14))
color_entry.pack()

# Button to start magic
start_button = tk.Button(root, text="Start Magic", font=('Arial', 14), bg='SystemButtonFace', command=start_magic)
start_button.pack(pady=20)

# Bind hover motion events to button
start_button.bind("<Enter>", on_enter)
start_button.bind("<Leave>", on_leave)

# Run the application
root.mainloop()

# Release the video capture object and close the OpenCV windows
if 'cap' in globals():
    cap.release()
cv2.destroyAllWindows()
