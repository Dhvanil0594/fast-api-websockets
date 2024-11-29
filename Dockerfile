# Use an official Python runtime as the base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI application code into the container
COPY . .

# Expose the port that FastAPI runs on
EXPOSE 8000

# # Add an entrypoint script to run migrations before starting the app
# COPY entrypoint.sh /entrypoint.sh
# RUN chmod +x /entrypoint.sh

# Command to run the entrypoint script
# CMD ["/entrypoint.sh"]
# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
