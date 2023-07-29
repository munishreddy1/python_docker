# Use an appropriate base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the backend server code into the container
COPY backend_server.py /app/

# Install the required dependencies
RUN pip install flask psycopg2 matplotlib

# Expose the port on which the Flask app will run
EXPOSE 5000

# Run the backend server
CMD [ "python", "backend_server.py" ]
