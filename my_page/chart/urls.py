from django.urls import path

from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("top_offers", views.top_offers, name="top_offers"),
    path("top_skills", views.top_skills, name="top_skills"),
    path("top_city", views.top_city, name="top_city"),
    path("city_to_work_on_site", views.city_to_work_on_site, name="city_to_work_on_site"),

]