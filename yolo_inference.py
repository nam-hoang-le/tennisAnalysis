from ultralytics import YOLO
import os

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

model = YOLO("models/yolov8x.pt")

model.track("data/vids/tennis_video.mp4", save=True)

