from unittest import TestCase

from pydantic import ValidationError
from shapely.geometry import Point

from python_basket_points.models import BBox, OrderPoint


class TestBBox(TestCase):
    def test_valid_bbox(self):
        bbox = BBox(min_x=-122.5247, min_y=37.4347, max_x=-122.3386, max_y=37.8206)
        self.assertEqual(bbox.min_x, -122.5247)
        self.assertEqual(bbox.min_y, 37.4347)
        self.assertEqual(bbox.max_x, -122.3386)
        self.assertEqual(bbox.max_y, 37.8206)

    def test_invalid_bbox(self):
        with self.assertRaises(ValidationError):
            _ = BBox(min_x=-122.5247, min_y=37.4347, max_x=-122.3386)  # type: ignore

    def test_from_list(self):
        bbox = BBox.from_list([-122.5247, 37.4347, -122.3386, 37.8206])
        self.assertEqual(bbox.min_x, -122.5247)
        self.assertEqual(bbox.min_y, 37.4347)
        self.assertEqual(bbox.max_x, -122.3386)
        self.assertEqual(bbox.max_y, 37.8206)

    def test_from_list_with_invalid_bbox(self):
        with self.assertRaises(ValueError):
            _ = BBox.from_list([-122.5247, 37.4347, -122.3386])

    def test_invalid_min_x(self):
        with self.assertRaises(ValidationError):
            _ = BBox(min_x=10, min_y=0, max_x=0, max_y=10)

    def test_invalid_min_y(self):
        with self.assertRaises(ValidationError):
            _ = BBox(min_x=0, min_y=10, max_x=10, max_y=0)


class TestOrderPoints(TestCase):
    def test_get_xy(self):
        order_point = OrderPoint(id=1, point=Point(5.5, 10.2))
        xy = order_point.get_xy()
        self.assertEqual(xy, [10.2, 5.5])
