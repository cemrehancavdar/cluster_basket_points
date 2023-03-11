from geojson import FeatureCollection, Feature
from python_basket_points.constants import MASLAK_BBOX, KMS_PER_RADIAN
from python_basket_points.generate_clusters import calculate_cluster_list

from python_basket_points.models import BBox, OrderPoint, ClusteredOrderPoint
from python_basket_points.utils import random_point_in_bbox, set_cluster_numbers
import itertools


def get_clustered_points(point_count: int, distance_in_km: float = 1) -> list[ClusteredOrderPoint]:
    bbox = BBox.from_list(MASLAK_BBOX)
    random_order_points = [OrderPoint(id=i, point=random_point_in_bbox(bbox=bbox)) for i in range(point_count)]

    epsilon = distance_in_km / KMS_PER_RADIAN

    clusters = calculate_cluster_list(epsilon=epsilon, points=random_order_points)

    clustered_order_points = set_cluster_numbers(random_order_points, clusters=clusters)

    return clustered_order_points


def clustered_points_to_feature_collection(order_points: list[ClusteredOrderPoint]) -> FeatureCollection:
    feature_list = [
        Feature(geometry=point.point, id=point.id, properties={"cluster": point.cluster_number})
        for point in order_points
    ]

    return FeatureCollection(feature_list)


def group_clustered_points(order_points: list[ClusteredOrderPoint]) -> dict[int, list[ClusteredOrderPoint]]:

    grouped_clusters = {}
    sorted_points = sorted(order_points, key = lambda point: point.cluster_number)
    
    for key, group in itertools.groupby(sorted_points, lambda point: point.cluster_number):
        grouped_clusters[key] = list(group)

    return grouped_clusters
