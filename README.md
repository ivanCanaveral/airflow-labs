# Airflow labs

Let's play with apache airflow!

### Components

Airflow has three components:

* Webserver
* Scheduler
* Database

### Docker and airflow

We will need to launch two processes (the webserver and the scheduler) inside our container. To launch both, we are going to use `supervisord` at `CMD`.

### Building the image

```bash
$ docker build . -t airflow
```

### Running the container

```bash
$ docker run -d -p 8080:8080 --name airflow --rm airflow:latest
```
