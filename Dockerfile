# Use an official Python runtime as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /workspace

# Copy the requirements file and install dependencies

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container
COPY my_page /workspace/my_page
COPY main.py /workspace/main.py
# Expose the port your Django app will run on
EXPOSE 8000

CMD ["cd", "my_page"]

# Specify the command to run your Django app
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]