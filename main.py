import cv2
from utils import read_video, save_video # importing from the folder directly because the functions have been exposed by the __init__.py in the folder
from trackers import Tracker

def main():
    # Read video
    video_frames = read_video("input_videos/08fd33_4.mp4")

    
    # Initialize tracker
    tracker = Tracker("models/best.pt")

    track = tracker.get_object_tracks(video_frames, read_from_stub=True, stub_path="stubs/track_stubs.pkl")

    # # Save cropped image of a player
    # for track_id, player in track['players'][0].items():
    #     bbox = player['bbox']
    #     frame = video_frames[0]

    #     # crop bbox from frame
    #     cropped_image = frame[int(bbox[1]):int(bbox[3]), int(bbox[0]):int(bbox[2])]

    #     # Save the cropped image
    #     cv2.imwrite(f"output_videos/cropped_image.jpg", cropped_image)
    #     break

    # Draw output 
    ## Draw object Tracks

    output_video_frames = tracker.draw_annotations(video_frames, track)

    # Save video
    save_video(output_video_frames, "output_videos/output_video.avi")
    

    

if __name__ == "__main__":
    main()