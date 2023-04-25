# Bank Customer Credit Score Prediction APP


## Instructions and Setup Guide

### Containerize the application using Docker

1. Build the Build the Docker Image

```bash
$ docker build  -t my-app .
```

2. Start the Container:

```bash
$ docker run -p 8000:8000 my-app
```

### Testing the application

1. Go to your web browser and visit http://0.0.0.0:8000 or the URL of the server where the Docker container is running.

2. You will see the home page of the application, where you can enter the details of a bank customer to predict their credit score.

3. Fill in the bank customer details in the form and click on "Submit".

4. You will see the predicted credit score for the bank customer on the screen.

### Local testing & examining logs

1. Find out the container id of the running container:

```bash
$ docker ps
```

This will return a response like the following:

```bash

CONTAINER ID   IMAGE                COMMAND                  CREATED         STATUS         PORTS                NAMES
f9b59902e94f   fastapi-ml   "uvicorn main:app --…"   10 minutes ago   Up 10 minutes   0.0.0.0:8000->8000/tcp   brave_liskov

```

2. SSH into the container using the container id from above:

```bash
$ docker exec -it <container id> /bin/sh
```

3. Tail the logs:

```bash
$ tail -f ../data/logs.out

```

### Shot down the docker

```bash
$ docker stop your_Container_id

```

