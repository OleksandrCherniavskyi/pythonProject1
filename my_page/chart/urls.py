from django.urls import path

from . import views

urlpatterns = [
    path("", views.main, name="main"),
    #path('find_most_popular_skill/', views.find_most_popular_skill, name='find_most_popular_skill'),
]