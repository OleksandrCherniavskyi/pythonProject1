from django.urls import path
from . import views

urlpatterns = [
    path("",  views.start, name="start"),
    path("week", views.week, name="week"),
    path("month", views.month, name="month"),
    path("quartal", views.quartal, name="quartal"),
    path("my_offers", views.my_offers, name="my_offers"),
]
