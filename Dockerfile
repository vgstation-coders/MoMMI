# Use a base image with Python and pip
FROM python:3.6

# Set the working directory in the container
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install Python requirements
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    cp config/example/* config/

# Expose any required port

# Command to run the Python application
CMD ["python", "main.py"]
