from django.urls import path
from .views import *
urlpatterns = [
    path("start/", startProcess.as_view(), name="start process")
]
