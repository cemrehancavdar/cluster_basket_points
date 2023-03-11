from pydantic import BaseModel, validator
from shapely.geometry import Point
from typing import Union


class BBox(BaseModel):
    min_x: float
    min_y: float
    max_x: float
    max_y: float

    @classmethod
    def from_list(cls, bbox: list[float]) -> "BBox":
        if len(bbox) != 4:
            raise ValueError("bbox must have exactly 4 values")
        return cls(min_x=bbox[0], min_y=bbox[1], max_x=bbox[2], max_y=bbox[3])

    @validator("max_x")
    def validate_min_x(cls, v, values):
        if v <= values["min_x"]:
            raise ValueError("min_x must be less than max_x")
        return v

    @validator("max_y")
    def validate_min_y(cls, v, values):
        if v <= values["min_y"]:
            raise ValueError("min_y must be less than max_y")
        return v


class OrderPoint(BaseModel):
    id: int
    point: Point
    cluster_number: Union[int, None] = None

    class Config:
        arbitrary_types_allowed = True

    def get_xy(self) -> list[float]:
        lon, lat = self.point.coords.xy
        return [lat[0], lon[0]]
