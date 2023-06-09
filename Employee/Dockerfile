# Use an official Python runtime as the base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip3 install -r requirements.txt

# Copy the application code into the container
COPY . .

# Set the environment variables, if needed
# ENV VARIABLE_NAME=value

# Expose the port on which your Flask application will run
EXPOSE 5000

# Specify the command to run your Flask application
CMD ["python", "app.py"]

