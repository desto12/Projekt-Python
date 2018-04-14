from django.urls import path

from . import views

urlpatterns = [
    path('', views.product_list, name='index'),
    path('detail/', views.product_detail, name='detail'),
]