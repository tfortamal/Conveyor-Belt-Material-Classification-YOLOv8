from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n-cls.pt')  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data='/Users/tamaldas/Desktop/DSS/cBelt/CustomDataSet/J1C1DataYOLO/classificationData/Data', epochs=20, imgsz=640)
