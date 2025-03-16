# Base image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy app files
COPY ./app /app
COPY requirements.txt /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
