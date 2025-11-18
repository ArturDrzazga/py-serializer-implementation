import json

from rest_framework import serializers

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(instance=car)
    json_string = json.dumps(serializer.data)
    return json_string.encode("utf-8")


def deserialize_car_object(json: bytes) -> Car:
    file = json.decode("utf-8")
    dict_data = json.loads(file)

    serializer = CarSerializer(data=dict_data)
    if serializer.is_valid():
        car_instance = serializer.save()
        return car_instance
    else:
        raise serializers.ValidationError(serializer.errors)
