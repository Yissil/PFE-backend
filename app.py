import logging
from flask import Flask, request, jsonify
from db import conn

# Set up logging
logging.basicConfig(filename='post_requests.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def post_data():
    data = request.json

    cursor = conn.cursor()
    
    # Prepare the SQL query and values based on the payload
    cursor.execute(
        """
        INSERT INTO data (HUMIDITY, TEMPERATURE1, TEMPERATURE2, TEMPERATURE3, PRESSURE, HEARTRATE, SPO2, IPV)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            data.get('humidity'),
            data.get('temperature1'),
            data.get('temperature2'),
            data.get('temperature3'),
            data.get('pressure'),
            data.get('heartrate'),
            data.get('spo2'),
            data.get('ipv')
        )
    )
    
    conn.commit()

    # Log the POST request data
    logging.info(f"POST request data: {data}")
    
    return jsonify({"message": "Data inserted successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
