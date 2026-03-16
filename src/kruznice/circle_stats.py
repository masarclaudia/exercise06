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

# test
from circle_stats import has_intersection, radius_sum

def test_has_intersection():

    assert has_intersection({"x":0, "y":0, "r":2}, {"x":3, "y":0, "r":2}) == {"is_intersection": True, "intersections_count": 2}
    assert has_intersection({"x":0, "y":0, "r":3}, {"x":2, "y":2, "r":2}) == {"is_intersection": True, "intersections_count": 2}


    assert has_intersection({"x":0, "y":0, "r":2}, {"x":4, "y":0, "r":2}) == {"is_intersection": True, "intersections_count": 1}
    assert has_intersection({"x":0, "y":0, "r":3}, {"x":3, "y":0, "r":0}) == {"is_intersection": True, "intersections_count": 1}


    assert has_intersection({"x":0, "y":0, "r":2}, {"x":5, "y":0, "r":2}) == {"is_intersection": False, "intersections_count": 0}

def test_radius_sum():

    assert radius_sum(3, 5) == 8