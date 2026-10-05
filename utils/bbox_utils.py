def get_center_of_bbox(bbox):
    """
    Given a bounding box in the format [x_min, y_min, x_max, y_max],
    return the center point (x_center, y_center).
    """
    x_min, y_min, x_max, y_max = bbox
    x_center = (x_min + x_max) / 2
    y_center = (y_min + y_max) / 2
    return int(x_center), int(y_center)

def get_bbox_width(bbox):
    """
    Given a bounding box in the format [x_min, y_min, x_max, y_max],
    return the width of the bounding box.
    """
    x_min, y_min, x_max, y_max = bbox
    width = x_max - x_min
    return width


def measure_distance(p1,p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

def measure_xy_distance(p1,p2):
    return p1[0]-p2[0],p1[1]-p2[1]

def get_foot_position(bbox):
    x1,y1,x2,y2 = bbox
    return int((x1+x2)/2),int(y2)