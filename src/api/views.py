import string
import random
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from .task import *
from rest_framework.response import Response
from manage.celery import app
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import fileSerializer, userDataSerializer
from .models import userData


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


# This for the data extraction for example 1 and 2 in which one can upload csv and server will map it to the database
# In parallel. in return user will get the task_id which one can user to stop the process
# POST Request:
# Data:
# {
#    "file": "file with file location"
# }
class uploadFile(APIView):
    parser_class = (FileUploadParser,)

    @staticmethod
    def post(request):
        # matching the data according to the database
        data = {
            "file": request.data["file"],
            "hash": ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        }

        file_serializer = fileSerializer(data=data)
        if file_serializer.is_valid():
            file_serializer.save()
            task = baselineDataUpload.delay(data["hash"])  # Starting the database upload
            return Response({"task_id": str(task)}, status=200)
        return Response({"msg": "Bad Request"}, status=400)


# this is api for example 2 in which one can extract data and file the extracted data in the form of csv
# this consists get and post request.
# get : restful api request for get the data on the dashboard
# post : it starts the request for extraction
# example Data:
# {
# 	"startDate":"2020-03-17",
# 	"endDate":"2020-03-17"
# }

class exportData(generics.ListAPIView):
    queryset = userData.objects.order_by("pk")
    serializer_class = userDataSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = "__all__"  # all filters are applied
    pagination_class = StandardResultsSetPagination

    @staticmethod
    def post(request):
        # This function creates the random name of the extraction csv file
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        obj = extractDataFields.delay(request.data, filename)  # call for the celery task

        # Response Data will be like:
        # {
        #     "task_id": "9bf97a06-1529-4fda-a8fb-89a4ad65b911",
        #     "link": "http://127.0.0.1:8000/media/S3BCJ8D.csv"
        # }
        #
        # here task_id returned will be used to control the operation
        return Response({"task_id": str(obj),
                         "link": "http://" + request.META['HTTP_HOST'] + "/media/" + filename + ".csv"}, status=200)


# this performs the operation stop operation Due to Lack of functionality of celery in windows, most of my time was
# gone into setup also, I messed up the ubuntu wsl because of the I was not able to add much functionality
class stopProcess(APIView):
    @staticmethod
    def post(request):
        app.control.revoke(request.data["id"])  # this will revoke the process
        return Response({"msg": "Process Stopped"}, status=200)
