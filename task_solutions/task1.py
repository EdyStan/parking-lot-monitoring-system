from ultralytics import YOLO
from shapely.geometry import Polygon, box, Point
import matplotlib.pyplot as plt
import cv2
import os


def solve_task1(TASK1_PATH, TASK1_OUTPUT_PATH):
    model = YOLO('yolov8n.pt')  
    print("Model loaded successfully")

    for file_name in os.listdir(TASK1_PATH):
        if not file_name.endswith('.jpg'):
            continue
        print(file_name)

        parking_lots_coords = [
            # Polygon 1
            [(1604, 842), (1750, 893), (1750, 1047), (1568, 1039)],
            # Polygon 2
            [(1472, 761), (1609, 783), (1552, 984), (1413, 923)],
            # Polygon 3
            [(1345, 683), (1472, 744), (1401, 889), (1270, 813)],
            # Polygon 4
            [(1357, 664), (1258, 603), (1170, 733), (1272, 798)],
            # Polygon 5
            [(1247, 608), (1158, 568), (1084, 669), (1170, 729)],
            # Polygon 6
            [(1167, 563), (1092, 510), (1006, 613), (1086, 657)],
            # Polygon 7
            [(1089, 518), (1019, 481), (943, 564), (1006, 608)],
            # Polygon 8
            [(1023, 481), (952, 562), (889, 522), (958, 456)],
            # Polygon 9
            [(958, 451), (886, 530), (835, 483), (911, 418)],
            # Polygon 10
            [(914, 422), (838, 495), (794, 451), (870, 403)]
        ]
        parking_lots_coords = [Polygon(coordinates) for coordinates in parking_lots_coords]
        
        input_img = cv2.imread(os.path.join(TASK1_PATH, file_name))
        results = model(input_img)
        boxes_coords = results[0].boxes.xyxy
        cls_indices = results[0].boxes.cls
        names_dict = results[0].names
        print(results[0].names[0])
        automobile_classes = ['car', 'truck']

        for coord, cls_idx in zip(boxes_coords, cls_indices):
            cls_name = names_dict[int(cls_idx)]
            if cls_name not in automobile_classes:
                continue
            x1, y1, x2, y2 = coord
            mid = Point((x1+x2) * 0.5, (y1+y2) * 0.5)

            for i, polygon in enumerate(parking_lots_coords):
                if polygon.contains(mid):
                    print("Haubau:", i+1)
                    break
            
            # print(f'Label:{cls_name}\ntop-left: {int(x1), int(y1)} bottom-right: {int(x2), int(y2)}\n')
        # annotated_image = results[0].plot()
        # output_image_path = os.path.join(TASK1_OUTPUT_PATH, file_name)
        # cv2.imwrite(output_image_path, annotated_image)
        break