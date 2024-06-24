import tkinter as tk
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk

def run_invisible_cloak():
    subprocess.Popen(["python", "Invisible_Cloak.py"])

def run_virtual_paint():
    subprocess.Popen(["python", "virtual_paint.py"])

def run_Facechange():
    subprocess.Popen(["python", "Facechange.py"])

def run_bgchanger():
    subprocess.Popen(["python", "bgchanger.py"])

def execute_selected_option():
    selected_option = var.get()
    if selected_option == 1:
        run_invisible_cloak()
    elif selected_option == 2:
        run_virtual_paint()
    elif selected_option == 3:
        run_Facechange()
    elif selected_option == 4:
        run_bgchanger()

# Initializing the window
# Convert WebP image to GIF
webp_img = Image.open(r"C:/Users/ANANTH/Pictures/aa1.jpg")
gif_img_path = "converted_image.gif"
webp_img.save(gif_img_path, "gif")

# Create the main window
root = tk.Tk()

# Initializing the window
root.title("Magic Cloak")
root.resizable(0, 0)

# Set window size and position
window_width = root.winfo_screenwidth() // 2
window_height = root.winfo_screenheight() // 2
root.geometry(f"{window_width}x{window_height}+0+0")

# Load background GIF image and resize
bg_img = Image.open(gif_img_path)
bg_img = bg_img.resize((window_width, window_height), Image.ANTIALIAS)

# Create a global variable to hold the PhotoImage object
bg_photo = ImageTk.PhotoImage(bg_img)

# Create a label with the background image
bg_photo = ImageTk.PhotoImage(bg_img)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a frame to hold the options
options_frame = tk.Frame(root, bg='lightblue')
options_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Create a label
label = tk.Label(options_frame, text="Choose an Option:", font=("Arial", 12), bg='lightblue')
label.pack(pady=10)

# Create radio buttons
var = tk.IntVar()
option1 = tk.Radiobutton(options_frame, text="Invisible Cloak", variable=var, value=1, font=("Arial", 10), bg='lightblue')
option2 = tk.Radiobutton(options_frame, text="Virtual Paint", variable=var, value=2, font=("Arial", 10), bg='lightblue')
option3 = tk.Radiobutton(options_frame, text="Facechange", variable=var, value=3, font=("Arial", 10), bg='lightblue')
option4 = tk.Radiobutton(options_frame, text="Backgroung Changer", variable=var, value=4, font=("Arial", 10), bg='lightblue')
option1.pack()
option2.pack()
option3.pack()
option4.pack()

# Create a button to execute the selected option
execute_button = tk.Button(options_frame, text="Execute", command=execute_selected_option, font=("Arial", 10), bg='green', fg='white')
execute_button.pack(pady=10)

# Run the application
root.mainloop()