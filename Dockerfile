# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the project dependencies
RUN pip install .

# Expose the port the app runs on
EXPOSE 8000

# Define the command to run the app using the click command
CMD ["python", "-m", "kitchengpt"]
