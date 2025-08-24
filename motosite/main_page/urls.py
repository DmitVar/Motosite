from django.urls import path,register_converter
from . import views
from . import converters

register_converter(converters.FourDigitConverter, 'year4') #регистрация кастомного конветора

urlpatterns =[
    path('', views.index, name='home'),
]

handler404 = views.handler404