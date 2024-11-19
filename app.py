import requests
from flask import Flask, render_template, request

app = Flask(__name__)

GOOGLEMAP_URL = "http://localhost:50215/get_coordinates"

@app.route("/", methods=["GET"])
def index():
    """Create the index.html page"""
    return render_template("index.html")

@app.route('/generate_map', methods=['GET', 'POST'])
def generate_map():
    """Handles the input for address and retrives the coordinates."""
    latitude = None
    longitude = None
    address = None

    if request.method == 'POST':
        query = request.form.get('query')
        if query:          
            # Make a GET request to the microservice
            response = requests.get(GOOGLEMAP_URL, params={'query': query})
            
            # Server has successfully processed the request and returned the requested data
            if response.status_code == 200:
                result = response.json()
                latitude = result['latitude']
                longitude = result['longitude']
                address = query
                print(f"Received coordinates: Latitude {latitude}, Longitude {longitude}")

    return render_template('generate_map.html', latitude=latitude, longitude=longitude, address=address)

if __name__ == "__main__":
    app.run(port=54141)
