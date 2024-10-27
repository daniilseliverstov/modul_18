from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_class_template, name='home'),
    path('class-template/', views.show_class_template, name='class_template'),
    path('function-template/', views.show_function_template, name='function_template'),
]
