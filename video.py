import numpy as np
import cv2
import os

SUPPORTED_VIDEO_FORMAT = (".mov")

def display_video(video_capture):
    delay = 25
    while True: 
        ret, frame = video_capture.read()
        
        if not ret:
            print("No more frames...")
            break
        
        cv2.imshow("Video", frame)
        if cv2.waitKey(delay) & 0xFF == 27: # 0xFF is the Esc key
            print("Esc key is pressed by user...")
            break
    # release the video capture object and close all windows
    video_capture.release()
    cv2.destroyAllWindows()

def main():
    video_path = input("Please enter path to a supported video file in .mov format or enter `quit` to exit: ")

    if video_path.lower() == "quit":
        print("Exiting the program...")
        return
    
    try:
        if not os.path.exists(video_path):
            print(f"Error: File does not exist - {video_path}")
            return
        
        if not video_path.lower().endswith(SUPPORTED_VIDEO_FORMAT):
            print(f"Error: Unsupported file format (supported formats are {SUPPORTED_VIDEO_FORMAT}) - {video_path}")
            return
        
        video_capture = cv2.VideoCapture(video_path)
        
        if not video_capture.isOpened():
            print(f"Error: Failed to open video file - {video_path}")
            return
        
        display_video(video_capture)
    
    except Exception as e:
        print(f"Error occured: {str(e)}")

if __name__ == "__main__":
    main()