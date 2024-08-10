import logging
from flask import Flask, request, jsonify
from db import conn
import ssl

# Set up logging
logging.basicConfig(filename='post_requests.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

app = Flask(__name__)

# Define SSL certificate and key file paths 
CERT_FILE = "cert.pem" 
KEY_FILE = "key.pem" 

# Create SSL context for server
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.minimum_version = ssl.TLSVersion.TLSv1_2
context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)

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
    app.run(host='0.0.0.0', port=5000, debug=True, ssl_context=context)