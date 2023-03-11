from shapely.geometry import Point
from .models import BBox, OrderPoint
import random


def random_point_in_bbox(bbox: BBox) -> Point:
    point = Point([random.uniform(bbox.min_x, bbox.max_x), random.uniform(bbox.min_y, bbox.max_y)])

    return point


def set_cluster_numbers(order_points: list[OrderPoint], cluster_numbers: list[int]) -> None:
    if len(order_points) != len(cluster_numbers):
        raise ValueError("Number of order points and number of cluster numbers do not match")

    for i, order_point in enumerate(order_points):
        order_point.cluster_number = cluster_numbers[i]
