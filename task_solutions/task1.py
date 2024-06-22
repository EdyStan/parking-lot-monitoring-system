from ultralytics import YOLO
from shapely.geometry import Polygon, Point
import cv2
import os


def solve_task1(TASK1_PATH, TASK1_OUTPUT_PATH, SHOW_DETAILS=False):
    model_names = ['yolov10n.pt', 'yolov8s.pt', 'yolov8m.pt']
    models = [YOLO(name) for name in model_names]

    parking_lots_coords = [
        # Parking lot 1
        [(1604, 842), (1750, 893), (1750, 1047), (1568, 1039)],
        # Parking lot 2
        [(1472, 761), (1609, 783), (1552, 984), (1413, 923)],
        # Parking lot 3
        [(1345, 683), (1472, 744), (1401, 889), (1270, 813)],
        # Parking lot 4
        [(1357, 664), (1258, 603), (1170, 733), (1272, 798)],
        # Parking lot 5
        [(1247, 608), (1158, 568), (1084, 669), (1170, 729)],
        # Parking lot 6
        [(1167, 563), (1092, 510), (1006, 613), (1086, 657)],
        # Parking lot 7
        [(1089, 518), (1019, 481), (943, 564), (1006, 608)],
        # Parking lot 8
        [(1023, 481), (952, 562), (889, 522), (958, 456)],
        # Parking lot 9
        [(958, 451), (886, 530), (835, 483), (911, 418)],
        # Parking lot 10
        [(914, 422), (838, 495), (794, 451), (870, 403)]
    ]
    parking_lots_coords = [Polygon(coordinates) for coordinates in parking_lots_coords]


    for file_name in os.listdir(TASK1_PATH):
        if not file_name.endswith('.jpg'):
            continue
        print(file_name)
        in_txt_path = os.path.join(TASK1_PATH, file_name[:-4] + '_query.txt')
        out_txt_path = os.path.join(TASK1_OUTPUT_PATH, file_name[:-4] + '_query.txt')
        with open(in_txt_path, 'r') as file:
            numbers = [int(line.strip()) for line in file.readlines()]

        first_number = numbers[0]

        rest_of_numbers = {num: 0 for num in numbers[1:]}

        automobile_classes = ['car', 'truck']
        input_img = cv2.imread(os.path.join(TASK1_PATH, file_name))
        for i, model in enumerate(models):
            results = model(input_img)
            boxes_coords = results[0].boxes.xyxy
            cls_indices = results[0].boxes.cls
            names_dict = results[0].names

            if SHOW_DETAILS:
                annotated_image = results[0].plot()
                output_image_path = os.path.join(TASK1_OUTPUT_PATH, f"{file_name[:-4]}_model{i}.jpg")
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
            file.write(str(first_number) + '\n')

            for i, key_value_pair in enumerate(rest_of_numbers.items()):
                if i != first_number - 1:
                    file.write(str(key_value_pair[0]) + ' ' + str(key_value_pair[1]) + '\n')
                else:
                    file.write(str(key_value_pair[0]) + ' ' + str(key_value_pair[1]))
                    
