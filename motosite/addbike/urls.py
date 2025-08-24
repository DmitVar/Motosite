from django.urls import path,register_converter
from . import views


urlpatterns =[
    path('', views.add_bike, name='add_bike'),
]