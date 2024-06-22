import cv2
import numpy as np

# Load an image
image = cv2.imread('/home/edstan/Desktop/master_AI/sem2/computer_vision/project2/train/Task1/06_2.jpg')

# Coordinates for parking lot polygons
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

# Convert list of coordinates to the format required by OpenCV
parking_lots_polygons = [np.array(coords, np.int32) for coords in parking_lots_coords]

overlay = image.copy()

# Color for the polygons (blue in BGR)
color = (255, 0, 0)
alpha = 0.4  # Transparency factor

# Fill the polygons on the overlay
for polygon in parking_lots_polygons:
    cv2.fillPoly(overlay, [polygon], color)

# Blend the overlay with the original image
cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)

# Draw the polygon borders on the final image
for polygon in parking_lots_polygons:
    cv2.polylines(image, [polygon], isClosed=True, color=(255, 0, 255), thickness=2)


# Display the image
cv2.imwrite('/home/edstan/Desktop/master_AI/sem2/computer_vision/project2/Parking_lots_highlighted.jpg', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
