from rest_framework import serializers

from django.core.validators import MaxValueValidator, MinValueValidator


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.IntegerField(
        validators=[MaxValueValidator(1914), MinValueValidator(1)]
    )
    is_broken = serializers.BooleanField()
