from django.urls import path
from . import views

app_name = "information"

urlpatterns = [
    path("", views.index, name = "index"),
    path("forecast", views.getForecast, name = "forecast"),
    path("key", views.getKey, name = "key"),
    path("city", views.getCity, name = "city")
]
