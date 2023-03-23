from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:category>/', views.index, name='index_with_category'),
]
