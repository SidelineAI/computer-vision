import cv2

def drop_every_third_frame(input_video_path, output_video_path):
    # Open the input video
    cap = cv2.VideoCapture(input_video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    codec = cv2.VideoWriter_fourcc(*'mp4v')  # Use appropriate codec for your needs

    # Create a VideoWriter object to write the output video
    out = cv2.VideoWriter(output_video_path, codec, fps, (width, height))

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break  # No more frames or error

        # Only write the frame if it's not the 3rd frame
        if (frame_count + 1) % 2 != 0:
            out.write(frame)

        frame_count += 1

    # Release everything
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("Processing complete. Output saved to", output_video_path)

# Example usage
input_video = '/home/tanush/Programming/Organizations/Sideline/computer-vision/datasets/SportsMOT/val/gh1.mp4'
output_video = '/home/tanush/Programming/Organizations/Sideline/computer-vision/datasets/SportsMOT/val/gh1_15fps.mp4'
drop_every_third_frame(input_video, output_video)
