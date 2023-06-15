from django.urls import path
from . import views

urlpatterns = [
    path("week", views.week, name="week"),
    path("month", views.month, name="month"),
    path("quartal", views.quartal, name="quartal"),

]
