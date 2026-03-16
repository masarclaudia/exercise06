import math

def radius_sum(r1, r2):
    return r1 + r2

def euclid_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def has_intersection(circle_1, circle_2):
    x1 = circle_1["x"]
    y1 = circle_1["y"]
    r1 = circle_1["r"]

    x2 = circle_2["x"]
    y2 = circle_2["y"]
    r2 = circle_2["r"]

    d = euclid_distance(x1, y1, x2, y2)
    s = radius_sum(r1, r2)
    diff = abs(r1 - r2)

    if math.isclose(d, s) or math.isclosed(d, diff):
        return {"is_intersection": True, "intersections_count": 1}
    if diff < d < s:
        return {"is_intersection": True, "intersections_count": 2}
    return {"is_intersection": False, "intersections_count": 0}