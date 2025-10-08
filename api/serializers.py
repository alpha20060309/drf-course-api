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


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name')
    product_price = serializers.DecimalField(source='product.price',max_digits=16,decimal_places=2)
    product_stock = serializers.IntegerField(source='product.stock')

    class Meta:
        model = OrderItem
        fields = (
            'product_name',
            'product_price',
            'product_stock',
            'quantity',
            'order',
            'item_subtotal'
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'orders'
        )

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(method_name='total')
    username = serializers.CharField(source='user.username')

    def total(self,obj):
        order_items = obj.items.all()
        return sum(order_item.item_subtotal for order_item in order_items)

    class Meta:
        model = Order
        fields = (
            'order_id',
            'created_at',
            'username',
            'status',
            'items',
            'total_price'
        )

class ProductInfoSerializer(serializers.Serializer):
    # get call products, count of products, max price
    products = Productserializer(many=True)
    count = serializers.IntegerField()
    max_price = serializers.FloatField()