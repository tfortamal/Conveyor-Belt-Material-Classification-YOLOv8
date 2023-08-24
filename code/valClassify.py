from ultralytics import YOLO

# Load the trained model
model = YOLO('/Users/tamaldas/Desktop/DSS/cBelt/YOLOv8ClassificationTesting/J1C1/runs/classify/train2/weights/best.pt')  # load a custom model

# Validate the model
metrics = model.val()  # no arguments needed, dataset and settings remembered
metrics.box.map    # map50-95
metrics.box.map50  # map50
metrics.box.map75  # map75
metrics.box.maps   # a list contains map50-95 of each category
