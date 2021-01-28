from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("<int:id>", views.index, name = "index"),
    path("home/", views.home, name = "home"),
    path("create/", views.create, name = "create"),
    path("thanks/", views.thanks, name = "thanks")
]