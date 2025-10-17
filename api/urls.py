from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('products/', views.ProductListCreateApiView.as_view()),
    path('products/<int:product_id>/', views.ProductDetailApiView.as_view()),
    path('product/info/', views.ProductInfoApiView.as_view()),
]
router = DefaultRouter()
router.register('orders', views.OrderViewSet)
urlpatterns += router.urls
