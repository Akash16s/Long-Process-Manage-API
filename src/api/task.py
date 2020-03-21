import os
from celery import shared_task
from manage.settings import BASE_DIR
from .models import filesModel, userData
import csv


# This function uploads the user data from the csv file
@shared_task
def baselineDataUpload(Hash):
    obj = filesModel.objects.get(hash=Hash)
    with open(os.path.join(BASE_DIR, "media/") + obj.file.name, 'r') as file:
        reader = list(file)
        for row in reader[1:]:
            row = list(row)
            userData.objects.create(
                userId=row[2],
                first_name=row[3],
                middle_name=row[4],
                last_name=row[5],
                date=row[6],
                phoneNumber=row[7]
            )
    return None


# This function extracts the user data into the csv file
@shared_task
def extractDataFields(data, name):
    startDate = data["startDate"]
    endDate = data["endDate"]
    Data = userData.objects.filter(date__gte=startDate, date__lte=endDate)
    with open(os.path.join(BASE_DIR, "media/") + name + '.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            ["id", "transactionHash", "userId", "first_name", "middle_name", "last_name", "date", "phoneNumber"])
        for data in Data:
            writer.writerow(
                [data.id, data.transactionHash, data.userId, data.first_name, data.middle_name, data.last_name,
                 data.date, data.phoneNumber])
    return None
