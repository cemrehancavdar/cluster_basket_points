from shapely.geometry import Point
from .models import BBox, OrderPoint, ClusteredOrderPoint
import random


def random_point_in_bbox(bbox: BBox) -> Point:
    point = Point([random.uniform(bbox.min_x, bbox.max_x), random.uniform(bbox.min_y, bbox.max_y)])

    return point


def set_cluster_numbers(order_points: list[OrderPoint], clusters: list[int]) -> list[ClusteredOrderPoint]:
    if len(order_points) != len(clusters):
        raise ValueError("Number of order points and number of cluster numbers do not match")

    clustered_order_points = [
        ClusteredOrderPoint(**point.dict(), cluster_number=clusters[i])
        for i, point in enumerate(order_points)
    ]

    return clustered_order_points
