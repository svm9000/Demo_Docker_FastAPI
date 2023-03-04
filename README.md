# Demo_Docker_FastAPI

## Table of Contents
1. [General Info](#1)
2. [Clone repo](#2)
3. [Build the Docker image](#3)
4. [Run the Docker image](#4)

<a name="1"></a>
## General Info
This repository contains:
  * Code to setup and demo the **FastAPI** framework, see [FastAPI](https://fastapi.tiangolo.com/) using [Docker](https://docs.docker.com/desktop/)
  * We also see how to setup the **Redis service** and **Debug server** for **VS Code**
  * Understand how to use **dataclass** and data type validation
  * We also illustrate how to use **docker-compose** to simplify the creation and running multi-container Docker applications

<a name="2"></a>
## 1. Clone repo
Clone the **files/folders** into your repo 
```
git clone https://github.com/svm9000/Demo_Docker_FastAPI.git

```
<a name="3"></a>
## 2. Build the Docker image
```console
$ docker build -t fastapi-image . 
```

<a name="4"></a>
## 3. Run the Docker image

```console
$ docker run -p 80:80 fastapi-image
```
or we can run in detached mode (background):

```console
$ docker run -d --name fastapicontainer -p 80:80 fastapi-image
```
`-p 80:80`: This binds the RHS `80` of the container to TCP port `80` on `127.0.0.1` of the host machine (local host). 

**Note:** we can also mount to a local directory for the container to have access all local files helps with persisting changes
```
docker run --name fastapicontainer -p 80:80 -d -v ${pwd}:/app fastapi-image
```
Host in Dockerfile must be:

`host: 0.0.0.0`: "placeholder", server to listen for and accept connections from any IP address.

The docker compose YAML file: `docker-compose.yaml` is used to configure the application’s services. 
Useful to start all the services with command:
```
docker-compose up
```
and stop and remove all **running containers** with:
```
docker-compose down
```

