# DevOps Lab 5 – Docker Images and Containers

## Project Overview
This project demonstrates how to build, run, and publish a Python application using Docker.

## Project Structure
```text
DevOps-Lab5-Docker/
├── Dockers/
│   ├── app.py
│   └── Dockerfile
└── .github/
    └── workflows/
        └── docker-build.yml
```

## Application
The Python application prints:

`Hello from inside Docker!`

## Docker Commands

Build the Docker image:
```bash
docker build -t my-python-app ./Dockers
```

Run the container:
```bash
docker run --name my-running-app my-python-app
```

Tag the image:
```bash
docker tag my-python-app navyamyadarapu/my-python-app:latest
```

Push the image to Docker Hub:
```bash
docker push navyamyadarapu/my-python-app:latest
```

## GitHub Actions
A GitHub Actions workflow automatically builds and pushes the Docker image to Docker Hub and runs a container for testing.

## Docker Hub
Docker Hub username: `navyamyadarapu`
