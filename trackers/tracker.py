from ultralytics import YOLO
import supervision as sv

class Tracker:
    def __init__(self, model_path):
        self.model = YOLO(model_path)
        self.tracker = sv.ByteTrack()

    def detect_frames(self, frames):
        batch_size = 20
        detections = []
        for i in range(0, len(frames), batch_size): # step size = 20 which is batch_size
            detections_batch = self.model.predict(frames[i:i+batch_size], conf=0.1) # prevent memory overload instead of self.model.predict(frames, conf=0.1) which attends to all frames at the same time 
            detections += detections_batch
            break
        return detections

    def get_object_tracks(self, frames):
        detections = self.detect_frames(frames)

        for frame_num, detection in enumerate(detections):
            cls_names = detection.names
            cls_names_inv = {v: k for k, v in cls_names.items()}

            # Convert to supervision detection format
            detection_supervision = sv.Detections.from_ultralytics(detection)

            # Convert GoalKeeper to player object
            for object_ind, class_id in enumerate(detection_supervision.class_id):
                if cls_names[class_id] == "goalkeeper":
                    detection_supervision.class_id[object_ind] = cls_names_inv['player']

            print(detection_supervision)

            break
