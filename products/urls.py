from django.urls import path
from . import views

app_name= 'products'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('product_creats/', views.product_creats, name='product_creats'),
]