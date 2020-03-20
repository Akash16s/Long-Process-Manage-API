from django.urls import path
from .views import *
urlpatterns = [
    path("baseUpload/", uploadFile.as_view(), name="baseline Upload"),
    path("extractData/", exportData.as_view(), name="dataExtract"),
    path("stop/", stopProcess.as_view(), name="stop process")
]
