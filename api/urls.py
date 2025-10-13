from django.urls import path,include
from . import views

urlpatterns = [
    path('products/', views.ProductListApiView.as_view()),
    path('products/<int:product_id>/', views.ProductDetailApiView.as_view()),
    path('product/info/', views.ProductInfoApiView.as_view()),
    path('orders/', views.OrderListApiView.as_view()),
    # path('users/', views.user_list),
    path('user-orders/', views.UserOrderListApiView.as_view(), name='user-orders'),
]
