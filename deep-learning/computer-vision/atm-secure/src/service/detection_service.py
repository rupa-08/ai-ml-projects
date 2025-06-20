from config import MODEL_PATH, DETECTION_THRESHOLD
from ultralytics import YOLO
import cv2

class DetectionService:
    def __init__(self, model_path: str=MODEL_PATH):
        self.model = YOLO(model_path)
        self.class_name = {0: "no_helmet", 1: "helmet"}

    def detect(self, image):
        results = self.model(image)[0]

        detection_classes = []
        for result in results.boxes.data.tolist():
            x1,y1,x2,y2,score,class_id = result

            if score >= DETECTION_THRESHOLD:
                class_name = self.class_name[int(class_id)]
                detection_classes.append(class_name)

                #draw boarding box in image
                cv2.rectangle(image, (int(x1),int(y1)), (int(x2),int(y2)),(0,255,0),2)

                #add class name text:
                cv2.putText(image, class_name, (int(x1), int(y1)-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

        return image, detection_classes