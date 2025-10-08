from django.urls import path,include
from . import views

urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:pk>/', views.product_detail),
    path('product/info/', views.product_info),
    path('orders/', views.order_list),
    path('users/', views.user_list),
]
