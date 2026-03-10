from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("novo/", views.criar_post, name="criar_post"),
]
