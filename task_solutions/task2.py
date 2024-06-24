from ultralytics import YOLO
from shapely.geometry import Polygon, Point
import cv2
import os


def solve_task2(TASK2_PATH, TASK2_OUTPUT_PATH, SHOW_DETAILS=False):
    model_names = ['yolov10n.pt', 'yolov8s.pt', 'yolov8m.pt']
    models = [YOLO(name) for name in model_names]

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


    for file_name in sorted(os.listdir(TASK2_PATH)):
        if not file_name.endswith('.mp4'):
            continue
        print(file_name)
        out_txt_path = os.path.join(TASK2_OUTPUT_PATH, file_name[:-4] + '_predicted.txt')

        input_vid = cv2.VideoCapture(os.path.join(TASK2_PATH, file_name))
        if not input_vid.isOpened():
            print("Error: Could not open video.")
            exit()

        
        last_frame = None

        while True:
            ret, frame = input_vid.read()
            if not ret:
                break
            last_frame = frame

        input_vid.release()

        rest_of_numbers = {num+1: 0 for num in range(10)}


        input_img = last_frame
        automobile_classes = ['car', 'truck']
        for i, model in enumerate(models):
            results = model(input_img)
            boxes_coords = results[0].boxes.xyxy
            cls_indices = results[0].boxes.cls
            names_dict = results[0].names
            print(results[0].names[0])

            if SHOW_DETAILS:
                annotated_image = results[0].plot()
                output_image_path = os.path.join(TASK2_OUTPUT_PATH, f"{file_name[:4]}_{i}.jpg")
                cv2.imwrite(output_image_path, annotated_image)


            for coord, cls_idx in zip(boxes_coords, cls_indices):
                cls_name = names_dict[int(cls_idx)]
                if cls_name not in automobile_classes:
                    continue
                x1, y1, x2, y2 = coord
                mid = Point((x1+x2) * 0.5, (y1+y2) * 0.5)

                for i in range(10):
                    if i+1 not in rest_of_numbers:
                        continue
                    if rest_of_numbers[i+1] != 1 and parking_lots_coords[i].contains(mid):
                        rest_of_numbers[i+1] = 1
                        break
        
        with open(out_txt_path, 'w') as file:
            for i, val in enumerate(rest_of_numbers.values()):
                if i != 9:
                    file.write(str(val) + '\n')
                else:
                    file.write(str(val))
                    
