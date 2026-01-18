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