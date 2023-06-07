from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("work_type/", views.work_type, name="work_type"),
]
