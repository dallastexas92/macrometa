from c8 import C8Client
import time
import requests
from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r'/latency/*': {'origins': '*'}})

# Replace with your Macrometa credentials and data-center URL
GEO_FABRIC = "_system"
API_KEY = "TlOIjb_faR4WiyVY8qOhBMQ.mykey.St6f2lRPOZp5OyiPk3eIQpL5r8NvNqhexBSibFZ7CDmFp3kMREpkhcHPYBzE0dg806e8dd" # Change this to your API key
DATA_CENTER_URL = 'sculpin-17899f79-us-southeast.paas.macrometa.io'

client = C8Client(protocol='https', host=DATA_CENTER_URL, port=443, apikey=API_KEY, geofabric=GEO_FABRIC)

@app.route('/latency', methods=['GET'])

def get_latency():
    
    start_time = time.time()
    # Perform a simple request to the GDN
    requests.get(f'https://{DATA_CENTER_URL}')

    end_time = time.time()
    latency = (end_time - start_time) * 1000  # Calculate latency in milliseconds
    return jsonify({'latency': latency})

if __name__ == '__main__':
    app.run(debug=True,port=5001)
