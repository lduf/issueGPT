# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script to the container
COPY scripts/ .

# Run the script when the container launches
CMD ["python", "/usr/src/app/process_issue.py"]
