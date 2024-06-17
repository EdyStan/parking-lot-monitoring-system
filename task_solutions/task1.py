from ultralytics import YOLO
import matplotlib.pyplot as plt
import cv2
import os


def solve_task1(TASK1_PATH, TASK1_OUTPUT_PATH):
    model = YOLO('yolov8n.pt')  
    print("Model loaded successfully")

    for file_name in os.listdir(TASK1_PATH):
        if not file_name.endswith('.jpg'):
            continue

        input_img = cv2.imread(os.path.join(TASK1_PATH, file_name))
        results = model(input_img)
        boxes = results[0].boxes
        coords = boxes.xyxy
        cls_names = boxes.cls
        print(cls_names)
        print(results[0].names[0])
        automobile_classes = ['car', 'truck']
        for box, cls_idx in zip(coords, cls_names):
            cls_name = results[0].names[int(cls_idx)]
            if cls_name not in automobile_classes:
                continue
            x1, y1, x2, y2 = box[0], box[1], box[2], box[3]
            
            print(f'Label:{cls_name}\ntop-left: {int(x1), int(y1)} bottom-right: {int(x2), int(y2)}\n')
        # annotated_image = results[0].plot()
        # output_image_path = os.path.join(TASK1_OUTPUT_PATH, file_name)
        # cv2.imwrite(output_image_path, annotated_image)
        # break