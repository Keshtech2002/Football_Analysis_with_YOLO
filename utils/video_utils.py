import cv2

def read_video(video_path):
    """
    Reads a video file and returns its frames as a list of numpy arrays.

    Args:
        video_path (str): Path to the video file.
    Returns:
        list: A list of frames, where each frame is represented as a numpy array.
    """
    cap = cv2.VideoCapture(video_path)
    frames = []
    if not cap.isOpened():
        raise IOError(f"Cannot open video file: {video_path}")
    
    while True:
        ret, frame = cap.read() # ret: boolean indicating if frame is read correctly, false means no frame to read again
        if not ret:
            break
        frames.append(frame)
    cap.release()
    
    return frames


def save_video(output_video_frames, output_video_path:str, fps=24.0):
    """
    Saves a list of frames as a video file.

    Args:
        output_video_frames (list): A list of frames, where each frame is represented as a numpy array.
        output_video_path (str): Path to save the output video file.
    """
    if not output_video_frames:
        raise ValueError("The list of video frames is empty.")
    
    height, width, layers = output_video_frames[0].shape
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # mp4v and so on 
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    for frame in output_video_frames:
        out.write(frame)
    
    out.release()