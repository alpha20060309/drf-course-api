from rest_framework import serializers
from .models import *

class Productserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'price',
            'stock'
            )

    def validate_price(self, value):
        if value <+ 0:
            raise serializers.ValidationError("Price must be positive")
        return value