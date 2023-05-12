# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

<<<<<<< HEAD
# Install MySQL client
RUN apt-get update && apt-get install -y default-mysql-client

=======
>>>>>>> d650c36583bab2ca738b69fe914b2e79c6112341
# Copy the application code
COPY . .

# Set environment variables
ENV FLASK_APP=app.py

# Expose the port on which the application will run
EXPOSE 5000

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]
