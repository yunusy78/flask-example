# Base image
FROM amopromo/python3.9-nginx
# Set working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
# Base image
FROM amopromo/python3.9-nginx

# Set working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
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
