# Use an appropriate base image
FROM python:3.9

# Install wait-for-it.sh
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/wait-for-it.sh

# Set the working directory in the container
WORKDIR /app

# Copy the server code into the container
COPY server.py /app/
COPY table.py /app/

# Install the required dependencies
RUN pip install psycopg2

# Start the server using wait-for-it.sh to wait for the database
CMD ["wait-for-it.sh", "db:5432", "--", "python", "./server.py"]


