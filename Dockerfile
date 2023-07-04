# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy the entire project directory into the container
COPY . .

# Specify the command to run your Django app
CMD ["python", "my_page/manage.py", "runserver", "0.0.0.0:8000"]