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
    cursor.execute(
        "INSERT INTO data (id, sensor, value_) VALUES (?, ?, ?)",
        (data['id'], data['sensor'], data['value_'])
    )
    conn.commit()

    # Log the POST request data
    logging.info(f"POST request data: {data}")
    
    return jsonify({"message": "Data inserted successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)