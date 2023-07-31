import time
import psycopg2

def connect_to_database(max_retries=10, retry_interval=5):
    retry_count = 0
    connected = False

    while retry_count < max_retries and not connected:
        try:
            # Try to connect to the database
            connection = psycopg2.connect(
                host='db',
                port='5432',
                database='postgres',
                user='postgres',
                password='password'
            )
            cursor = connection.cursor()
            connected = True
            print("Connected to the database successfully!")
        except psycopg2.OperationalError as e:
            print(f"Failed to connect to the database: {e}")
            print(f"Retrying in {retry_interval} seconds...")
            retry_count += 1
            time.sleep(retry_interval)

    if not connected:
        print("Unable to connect to the database after multiple retries. Exiting...")
        exit(1)

    return connection, cursor

def create_table():
    # Connect to the database with retries
    connection, cursor = connect_to_database()

    # Define the SQL statement to create the table
    create_table_query = '''
        CREATE TABLE sensor_data2 (
            id SERIAL PRIMARY KEY,
            temperature FLOAT NOT NULL,
            humidity INT NOT NULL,
            timestamp TIMESTAMP DEFAULT NOW()
        )'''

    # Execute the CREATE TABLE statement
    cursor.execute(create_table_query)

    # Commit the changes
    connection.commit()

    # Close the cursor and the connection
    cursor.close()
    connection.close()

    print("Table created successfully!")


if __name__ == '__main__':
    print("Creating table...")
    create_table()
