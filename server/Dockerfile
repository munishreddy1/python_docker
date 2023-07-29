# Use an appropriate base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the server code into the container
COPY server.py /app/
COPY table.py /app/

# Install the required dependencies
RUN pip install psycopg2

#Run the table.py for creating the table in database
RUN python table.py

# Run the server script when the container starts
CMD [ "python", "./server.py" ]

