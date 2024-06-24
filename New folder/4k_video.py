import cv2 

# Define a video capture object 
vidcap = cv2.VideoCapture(r"C:\Users\ANANTH\Desktop\New folder\fun.mp4") 

# Capture video frame by frame 
success, frame = vidcap.read() 

# Define the desired resolution (4K)
desired_width = 700
desired_height = 500

# Create VideoWriter object to save the resized video
output_video = cv2.VideoWriter('output_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (desired_width, desired_height))

# Creating a loop for running the video 
# and resizing all the frames 
while success: 
    # Resize the frame to 4K resolution
    resized_frame = cv2.resize(frame, (desired_width, desired_height))
    
    # Write the resized frame to the output video file
    output_video.write(resized_frame)
    
    # Display the resized frame (optional)
    cv2.imshow("Resized Frame", resized_frame)
    
    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    # Capture the next frame
    success, frame = vidcap.read() 

# Release the video capture and writer objects
vidcap.release()
output_video.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
