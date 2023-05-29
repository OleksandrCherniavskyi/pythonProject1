from django.urls import path

from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("top_offers", views.top_offers, name="top_offers"),
    path("top_skills", views.top_skills, name="top_skills"),

]