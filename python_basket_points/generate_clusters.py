from sklearn.cluster import AgglomerativeClustering
from python_basket_points.models import OrderPoint
import numpy as np


def calculate_cluster_list(epsilon: float, points: list[OrderPoint]) -> list[int]:
    dbscan = AgglomerativeClustering(n_clusters=None, distance_threshold=epsilon, compute_full_tree=True)  # type: ignore
    radians = np.radians([point.get_xy() for point in points]) # type: ignore
    return dbscan.fit_predict(radians).tolist()
