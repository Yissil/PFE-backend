from flask import Flask, jsonify
from db import conn

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM YourTable')
    rows = cursor.fetchall()
    data = [dict(zip([column[0] for column in cursor.description], row)) for row in rows]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)