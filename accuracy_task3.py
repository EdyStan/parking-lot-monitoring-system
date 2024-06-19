def parse_line(line):
    """Parse a line from the file into index and coordinates."""
    parts = line.strip().split()
    index = int(parts[0])
    x1 = int(parts[1])
    y1 = int(parts[2])
    x2 = int(parts[3])
    y2 = int(parts[4])
    return index, x1, y1, x2, y2

def calculate_area(x1, y1, x2, y2):
    """Calculate the area of a rectangle given its coordinates."""
    return (x2 - x1) * (y2 - y1)

def calculate_intersection_over_union(file1, file2, iou_threshold=0.3):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()[1:]  # skip the first line (header)
        lines2 = f2.readlines()[1:]  # skip the first line (header)

        total_iou = 0.0
        total_pairs = 0
        true_positives = 0

        for line1, line2 in zip(lines1, lines2):
            index1, x1_1, y1_1, x2_1, y2_1 = parse_line(line1)
            index2, x1_2, y1_2, x2_2, y2_2 = parse_line(line2)

            # Calculate coordinates of intersection
            inter_x1 = max(x1_1, x1_2)
            inter_y1 = max(y1_1, y1_2)
            inter_x2 = min(x2_1, x2_2)
            inter_y2 = min(y2_1, y2_2)

            # Check if there is intersection
            if inter_x1 < inter_x2 and inter_y1 < inter_y2:
                # Calculate intersection area
                inter_area = calculate_area(inter_x1, inter_y1, inter_x2, inter_y2)

                # Calculate union area
                union_area = (calculate_area(x1_1, y1_1, x2_1, y2_1) + calculate_area(x1_2, y1_2, x2_2, y2_2)) - inter_area

                # Calculate IOU
                iou = inter_area / union_area
            else:
                iou = 0.0  # no intersection

            print(f"IOU for line {index1} and {index2}: {iou:.4f}")
            
            total_iou += iou
            total_pairs += 1

            # Check if IOU is above the threshold
            if iou > iou_threshold:
                true_positives += 1

        if total_pairs > 0:
            average_iou = total_iou / total_pairs
            accuracy = true_positives / total_pairs
            print(f"Average IOU: {average_iou:.4f}")
            print(f"Accuracy (IOU > {iou_threshold}): {accuracy:.4f}")
        else:
            print("No valid pairs found.")

# Example usage
file1 = '/home/edstan/Desktop/master_AI/sem2/computer_vision/project2/output_train/Task3/01.txt'
file2 = '/home/edstan/Desktop/master_AI/sem2/computer_vision/project2/train/Task3/ground-truth/01_gt.txt'
calculate_intersection_over_union(file1, file2)
