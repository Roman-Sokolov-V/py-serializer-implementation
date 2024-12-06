from typing import io

from car.models import Car
from car.serializers import CarSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(json: bytes) -> Car:
    steam = io.BytesIO(json)
    data = JSONParser().parse(steam)
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        car = serializer.save()
        return car
    else:
        raise ValueError(f"Invalid data: {serializer.errors}")
