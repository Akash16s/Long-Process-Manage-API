# Long-Process-Manage-API
Task provided was to manage the task for time-taking and computation expensive process using API's.

## Idea
In local machine we can manage a asynchronous task using multithreading in python because the threads can access the data space of *main thread* in memory on every call through an API.

But on the sever every call have different thread associated with it, so instance of threading class will not be available for the next request to come.

The Solution is to have a pre-running process like *CELERY* which listens to the *Messaging Queue* like *redis* or *RabbitMQ*.

Steps:
* 1. First *API* call will initiate the process and in respose it will return the *task_id*.
* 2. Then *Celery* will start processing the task and save the results of the task in file or database through which the user can fetch the data.
* 3. If user wants to cancel the task, he/she can *Call* the request to revoke the process by providing *task_id* with the call.



# API:


```http://127.0.0.1:8000/api/baseUpload/```
Base API for csv upload and mapping the user
#### POST:
```
{
    "file":file
}
```

```http://127.0.0.1:8000/api/extractData/``` Extracting-Data api for getting the Users
#### GET: (Restful Request) User Data
#### POST:
```
{
    "startDate":"2020-03-16",
    "endDate":"2020-03-17"	
}
```

```http://127.0.0.1:8000/api/stop/ ``` API to stop the process
#### POST:
```
{
    "task_id": "f2e35b64-48dd-48fd-8856-bd207de820e7"
}
```
# On Further Extenstion
* Sever can have a mapping of the all the changes the revert it when the user revokes the process. 

* Also server can have a better stopping procedure using controlled process execution in celery.
