from shapely.geometry import Point
from python_basket_points.models import BBox
from unittest import TestCase

from python_basket_points.utils import random_point_in_bbox


class TestBBox(TestCase):
    def test_random_point_in_bbox(self):
        bbox = BBox(min_x=0, max_x=10, min_y=0, max_y=10)

        for _ in range(10):
            point = random_point_in_bbox(bbox)

            assert isinstance(point, Point)
            assert bbox.min_x <= point.x <= bbox.max_x
            assert bbox.min_y <= point.y <= bbox.max_y
