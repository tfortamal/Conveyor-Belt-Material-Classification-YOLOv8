
from ultralytics import YOLO
import cv2

# importting the trained model
model = YOLO("/Users/tamaldas/Desktop/DSS/cBelt/YOLOv8ClassificationTesting/J1C1/runs/classify/train2/weights/best.pt")

# taking video input
vid = "/Users/tamaldas/Desktop/DSS/cBelt/cBeltVideoData/J1C1/pallet_j1c1/3.mp4"
video_path = cv2.VideoCapture(vid)

# iterate through each frame
while True:
    ret, frame = video_path.read()

    # if there is no frame, beak out of the loop end the program 
    if not ret:
        break

    # Perform object detection
    results = model.predict(source=frame, show=False, save=False, save_txt=False)
    
    # print the class names
    clsNameDict = results[0].names
    print("class names: ", clsNameDict)

    # print detected class ID   
    id = results[0].probs.top1
    print("Detected Class ID: ", id)
    
    # print detected class name
    clsName = results[0].names[id]
    print("Detected Class Name: ", clsName)

    # writing info on image
    font = cv2.FONT_HERSHEY_DUPLEX
    string = "Detected Material: "+clsName
    cv2.putText(frame, string, (50, 100), font, 1, (255, 255, 0), 2, cv2.LINE_AA)

    # Display the annotated frame
    cv2.imshow("Classification", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#cv2.destroyAllWindows()
