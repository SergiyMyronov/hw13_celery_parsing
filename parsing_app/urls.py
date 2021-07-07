from django.urls import path

from parsing_app import views

urlpatterns = [
    path('', views.index, name='index'),
]
