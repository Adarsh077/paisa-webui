# Use the official Python image from the Docker Hub
FROM python:3.13.3-alpine

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the default command to run main.py
CMD ["streamlit", "run", "main.py", "--server.port=8003", "--server.address=0.0.0.0"]
