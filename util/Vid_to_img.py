import cv2
import os
import argparse

def extract_frames(video_path, output_path, fps_divider):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Initialize a frame counter
    frame_count = 0
    extract_count = 0

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
            frame_filename = os.path.join(output_path, f"frame_{frame_count:04d}.jpg")
            cv2.imwrite(frame_filename, frame)
            extract_count += 1

        # Increment the frame counter
        frame_count += 1

    # Release the video file
    cap.release()

    print(f"{extract_count} frames extracted and saved to {output_path}")

if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Extract frames from a video.")
    parser.add_argument("--video_path", help="Path to the video file", required=True)
    parser.add_argument("--output_path", help="Output directory for the images", required=True)
    parser.add_argument("--fps_divider", type=int, help="Extract every Nth frame", required=True)

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the function with the provided arguments
    extract_frames(args.video_path, args.output_path, args.fps_divider)
