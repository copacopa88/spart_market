from django.urls import path
from . import views

app_name= 'products'

urlpatterns = [
    path('', views.index, name='index'),
    path('product_creats/', views.product_creats, name='product_creats'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('<int:pk>/update', views.product_update, name='product_update'),
    path('<int:pk>/delete', views.product_delete, name='product_delete'),
    path("<int:pk>/comments/", views.comment_create, name="comment_create"),
    path("<int:pk>/comments/<int:comment_pk>/delete/", views.comment_delete, name="comment_delete"),
    path('<int:pk>/like/', views.like, name='like'),
]