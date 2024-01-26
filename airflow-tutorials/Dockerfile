# Use an official Python runtime as a parent image
FROM python:3.9.18

# Set the working directory in the container
WORKDIR /usr/src/app

# # Install Airflow
# RUN pip install apache-airflow==2.8.1
# ENV PATH="${PATH}:/root/.local/bin"
RUN pip install --upgrade pip

# Install Poetry
RUN pip install poetry==1.7.1
# RUN pip install scikit-learn==1.4.0

# Configure Poetry
RUN poetry config virtualenvs.create false

# Copy the project files into the working directory
COPY pyproject.toml poetry.lock* /usr/src/app/

# Install project dependencies
RUN poetry install --no-dev



# Copy the rest of the application code
# COPY . /usr/src/app


# # Start with the Apache Airflow image
# FROM apache/airflow:2.8.1

# # # Use an official Python runtime as a parent image
# # FROM python:3.9.18

# # Set the working directory in the container
# WORKDIR /usr/src/app

# # Install Poetry
# RUN pip install poetry==1.7.1  # Specify your desired version of Poetry here

# # Copy the project files into the working directory
# COPY pyproject.toml poetry.lock* /usr/src/app/

# # Configure Poetry
# RUN poetry config virtualenvs.create false

# # Install project dependencies
# RUN poetry install --no-dev  # Exclude development dependencies

# # Copy the rest of the application code
# COPY . /usr/src/app

# # Command to run on container start
# # CMD ["python", "your_app_script.py"]
