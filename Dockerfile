# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /api_for_query_coury_data

# Copy the current directory contents into the container at /app
COPY . /api_for_query_coury_data

RUN pip install --upgrade pip setuptools wheel --user
RUN pip install -r requirements.txt


# Run app.py when the container launches
CMD ["python", "app.py"]


