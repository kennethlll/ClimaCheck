from django.urls import path
from . import views

app_name = "alert"

urlpatterns = [
    path("", views.index, name = "index"),
    path("notification", views.sendEmail, name = "notification")
]