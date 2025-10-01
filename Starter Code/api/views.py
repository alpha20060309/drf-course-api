from django.shortcuts import get_object_or_404
from api.serializers import Productserializer, OrderSerializer, OrderItemSerializer,UserSerializer
from api.models import Product, Order, OrderItem,User
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = Productserializer(products, many=True)
    return Response(serializer.data,200)


@api_view(['GET'])
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = Productserializer(product)
    return Response(serializer.data,200)


@api_view(['GET'])
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data,200)

@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data,200)