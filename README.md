# Rabbit
Rabbit is a lightweight WSGI web application framework. Right now is a simple project to learn how a framework works.


```python
from rabbit import Rabbit, Response, Request

# Define rabbit object
rabbit = Rabbit(__name__)

def hello_from_rabbit(request: Request) -> Response:
    return Response("Hello from rabbit route!!!")

# Add new route to rabbit, the method and the function to call
rabbit.add_route("GET", "/hello", hello_from_rabbit)
```

To test the microframework, install Gunicorn WSGI (https://gunicorn.org/#docs)
```console
pip install gunicorn
```

Run the application executing run.sh file inside src folder
```
./run.sh

[2023-03-09 10:27:31 +0100] [9961] [INFO] Starting gunicorn 20.1.0
[2023-03-09 10:27:31 +0100] [9961] [INFO] Listening at: http://127.0.0.1:8000 (9961)
[2023-03-09 10:27:31 +0100] [9961] [INFO] Using worker: sync
[2023-03-09 10:27:31 +0100] [9962] [INFO] Booting worker with pid: 9962
[2023-03-09 10:27:31 +0100] [9963] [INFO] Booting worker with pid: 9963
[2023-03-09 10:27:31 +0100] [9964] [INFO] Booting worker with pid: 9964
[2023-03-09 10:27:31 +0100] [9965] [INFO] Booting worker with pid: 9965
```

Open your browser and go to gunicorn listening route (output of the run.sh) /hello
http://127.0.0.1:8000/hello

Check that "Hello from rabbit!" is displayed on the page
