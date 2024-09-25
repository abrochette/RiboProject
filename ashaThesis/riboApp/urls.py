from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("view1/", views.view1, name="view1"),
    path("", views.home, name="home"),
    path("create/", views.create, name="create")
]
