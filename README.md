## Used Database for storing raw sensor data

In this approach I the server fetches sensor data from a PostgreSQL database, performs data processing, and provides access to the processed data via an API.

## Features

- Fetches the last 10 entries of sensor data from a PostgreSQL database.
- Calculates the average temperature and average humidity of the fetched data.
- Provides access to the processed data through a RESTful API.

## Requirements

- Python 3.x
- PostgreSQL database(Preferably docker container)
- pgadmin provides GUI for postgreSQL.
- Required Python packages (specified in `requirements.txt`)

## Execution

- run docker-compose up --build. It will build the images using docker files and run the containers.
- Created custom docker network to create connectivity
