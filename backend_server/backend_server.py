import matplotlib.pyplot as plt
from flask import Flask, jsonify, send_file
import psycopg2
import os
import matplotlib

matplotlib.use('Agg')

app = Flask(__name__)

# Connect to the PostgreSQL database
connection = psycopg2.connect(
    host='db',
    port='5432',
    database='postgres',
    user='postgres',
    password='password'
)

# Create a cursor object
cursor = connection.cursor()

def fetch_sensor_data():
    # Fetch the last 10 entries from the database
    query = "SELECT temperature, humidity FROM sensor_data2 ORDER BY timestamp DESC LIMIT 10"
    cursor.execute(query)
    rows = cursor.fetchall()

    # Calculate average and mean
    total_temperature = 0
    total_humidity = 0
    for row in rows:
        temperature, humidity = row
        total_temperature += temperature
        total_humidity += humidity
    average_temperature = total_temperature / len(rows)
    average_humidity = total_humidity / len(rows)

    # Find highest and lowest values
    highest_temperature = max(rows, key=lambda x: x[0])[0]
    lowest_temperature = min(rows, key=lambda x: x[0])[0]
    highest_humidity = max(rows, key=lambda x: x[1])[1]
    lowest_humidity = min(rows, key=lambda x: x[1])[1]

    # Updated plot path to store at the root level plots folder in the container
    plot_path = '/app/plots/plot.png'

    # If a previous plot exists, remove it before generating a new one
    if os.path.exists(plot_path):
        os.remove(plot_path)

    # Generate the plot
    temperatures = [row[0] for row in rows]
    humidities = [row[1] for row in rows]
    plt.plot(temperatures, label='Temperature')
    plt.plot(humidities, label='Humidity')
    plt.xlabel('Entry')
    plt.ylabel('Value')
    plt.title('Sensor Data')
    plt.legend()

    # Save the plot to the specified path
    plt.savefig(plot_path)
    plt.close()

    # Prepare the response data
    processed_data = {
        'average_temperature': average_temperature,
        'average_humidity': average_humidity,
        'highest_temperature': highest_temperature,
        'lowest_temperature': lowest_temperature,
        'highest_humidity': highest_humidity,
        'lowest_humidity': lowest_humidity
    }

    return processed_data

@app.route('/api/processed-data')
def get_processed_data():
    data = fetch_sensor_data()
    return jsonify(data)

@app.route('/plot')
def get_plot():
    plot_path = '/app/plots/plot.png'  # Direct path to the plot in the container
    return send_file(plot_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


