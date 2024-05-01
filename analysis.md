detect and track the player as well as the tennis ball 

court key points -> player distance, ball is in or out 

-> output -> how many times player has shot the ball, how fast he shot it 
player speed, how many meters the player covered 

train two CNN: YOLO -> fast moving tennis ball 
CNN -> train to estimate the court key points -> PyTorch 

Train yolov5 with [Tennis dataset](https://universe.roboflow.com/viren-dhanwani/tennis-ball-detection/dataset/6#)

train to detect the tennis ball 

use yolov8x to track the player 

Tennis Court Detector [](https://github.com/yastrebksv/TennisCourtDetector?tab=readme-ov-file)

tracker -> player -> rectangle id player -> pkl file -> ball tracker -> rectangle 

court line and points, a little bit less corrected