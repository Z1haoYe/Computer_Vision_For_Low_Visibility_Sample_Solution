import cv2
import os

# Path to the video file
video_path = 'E:\seris\data\\fog_30_deg_circle3\\fog_30_deg_circle3.MP4'

# Output directory for the images
output_dir = 'E:\seris\data\\fog_30_deg_circle3\IMG_d10'

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Open the video file
cap = cv2.VideoCapture(video_path)

# Initialize a frame counter
frame_count = 0
extract_count = 0

# Number of frames to skip before extracting a frame
fps_divider = 10  # Adjust this value as needed

# Loop through the video frames
while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Break the loop if we have reached the end of the video
    if not ret:
        break

    # Check if it's time to save the frame based on the fps
    if frame_count % fps_divider == 0:
        # Save the frame as an image
        frame_filename = os.path.join(output_dir, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)
        extract_count += 1

    # Increment the frame counter
    frame_count += 1

# Release the video file
cap.release()

print(f"{extract_count} frames extracted and saved to {output_dir}")