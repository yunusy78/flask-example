# Base image
FROM docker.io/library/python:3.9-slim@sha256:1fc44d17b4ca49a8715af80786f21fa5ed8cfd257a1e14e24f4a79b4ec329388
# Set working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .
RUN pip install selenium

# Install dependencies
RUN pip install -r requirements.txt
# Install MySQL client
RUN apt-get update && apt-get install -y default-mysql-client

# Copy the application code
COPY . .

# Set environment variables
ENV FLASK_APP=app.py

# Expose the port on which the application will run
EXPOSE 5000

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]
