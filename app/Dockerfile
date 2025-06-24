 # Use the official Python image as the base
FROM python:3.13-bullseye
 # Set the working directory inside the container
WORKDIR /app
# Copy the Python script into the container at the working directory
COPY m1.py .
# Specify the command to run when the container starts
    CMD ["python", "m1.py"]
# Build Docker
## (.venv) PS C:\Users\oleg.pinchuk\PyCharmMiscProject\app> docker build -t m1 .
# Add tag to Docker
##  PS C:\Users\oleg.pinchuk\PyCharmMiscProject\app> docker tag m1 olegroyal/m1
# Push the Docker to Docker Hub
##  C:\Users\oleg.pinchuk\PyCharmMiscProject\app> docker push olegroyal/m1