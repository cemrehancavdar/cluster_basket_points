from fastapi import APIRouter

from python_basket_points.logic import (
    get_clustered_points,
    clustered_points_to_feature_collection,
    group_clustered_points,
)

router = APIRouter()


@router.get("/cluster")
def cluster(count: int = 500):
    clustered_points = get_clustered_points(point_count=count)
    feature_collection = clustered_points_to_feature_collection(clustered_points)
    return feature_collection


@router.get("/cluster/group")
def grouped_cluster(count: int = 500):
    clustered_points = get_clustered_points(point_count=count)
    grouped_clusters = group_clustered_points(clustered_points)
    return grouped_clusters
