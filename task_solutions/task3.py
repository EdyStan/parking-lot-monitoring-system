from ultralytics import YOLO
from shapely.geometry import Polygon, Point
import cv2
import os


def solve_task3(TASK3_PATH, TASK3_OUTPUT_PATH):
    # initialize model
    model = YOLO('yolov8n.pt')  
    print("Model loaded successfully")

    for file_name in sorted(os.listdir(TASK3_PATH)):
        if not file_name.endswith('.mp4'):
            continue
        print(file_name)

        # initialize the paths
        tracker_init_path = os.path.join(TASK3_PATH, file_name[:-4] + '.txt')
        out_txt_path = os.path.join(TASK3_OUTPUT_PATH, file_name[:-4] + '.txt')

        # get the initial coordinates of the vehicle we want to track
        with open(tracker_init_path, 'r') as tracker_file:
            tracker_lines = tracker_file.readlines()
        if len(tracker_lines) >= 2:
            values = tracker_lines[1].strip().split()
            _, xi1, yi1, xi2, yi2 = map(int, values)
            xi_mean = (xi1+xi2) * 0.5
            yi_mean = (yi1+yi2) * 0.5

        tracker_initialized = False
        trace = []

        # capture video and loop through its frames
        input_vid = cv2.VideoCapture(os.path.join(TASK3_PATH, file_name))
        while input_vid.isOpened():
            # read the frame and check if the read is valid
            success, input_img = input_vid.read()
            if not success:
                break
            
            # apply the model on the image and extract the bounding boxes coordinates
            results = model(input_img)
            boxes_coords = results[0].boxes.xyxy

            if not tracker_initialized:
                # Find the closest bounding box to the initial point
                min_distance = float('inf')
                closest_box = None
                for coord in boxes_coords:
                    x1, y1, x2, y2 = coord
                    x_mean = (x1+x2) * 0.5
                    y_mean = (y1+y2) * 0.5
                    l1_distance = (abs(x_mean - xi_mean) + abs(y_mean - yi_mean))
                    if l1_distance < min_distance:
                        min_distance = l1_distance
                        closest_box = coord

                if closest_box is not None:
                    # Initialize the tracker with the closest bounding box
                    tracker = cv2.TrackerCSRT_create()  # or use any other tracker
                    tracker.init(input_img, (int(closest_box[0]), int(closest_box[1]), int(closest_box[2] - closest_box[0]), int(closest_box[3] - closest_box[1])))
                    # tracker.init(input_img, closest_box)
                    tracker_initialized = True
                    trace.append((int(closest_box[0]), int(closest_box[1]), int(closest_box[2]), int(closest_box[3])))

            else:
                # update the tracker and save the trace
                success, box = tracker.update(input_img)
                if success:
                    print(box)
                    trace.append(box)

        length = len(trace)
        with open(out_txt_path, 'w') as file:
            # Write the header
            file.write(f"{length} -1 -1 -1 -1\n")
            
            # Write each index and tuple in the desired format
            for index, (x1, y1, x2, y2) in enumerate(trace):
                file.write(f"{index} {x1} {y1} {x1 + x2} {y1 + y2}\n")