# CS361_Google_Map_API
1. Overview
   
This microservice allows a user to search for a company's location based on the name of its headquarters/ its street address. It uses the Google Maps API to retrieve geolocation data that includes the latitude and longitude, and returns a JSON response with the results. Then it uses flask to render a map displaying the retrieved location in a html page. 

2. Request Format:

Query parameter: query (required): The address or location name to search for.


How to Send the Request:

Send a GET request to http://localhost:50215/get_coordinates with the query parameter query.
```
import requests

GOOGLEMAP_URL = "http://localhost:50215/get_coordinates"
query = "1600 Amphitheatre Pkwy, Mountain View, CA 94043"

response = requests.get(GOOGLEMAP_URL, params={'query': query})

if response.status_code == 200:
    result = response.json()
    print("Latitude:", result['latitude'])
    print("Longitude:", result['longitude'])
else:
    print("Error:", response.json().get('error', 'Location not found'))

```

Expected Response when the microservice return a JSON response containing the latitude and longitude.
```
{
  "latitude": 37.422,
  "longitude": -122.084801
}
```
Expected Response when an error occur.
```
{
  "error": "Location does not exist"
}
```
3. Receive format:
   
The Flask application (app.py) interacts with the microservice by sending a GET request to retrieve geolocation data and then renders it on an HTML page.
#Example of receiving data
```
response = requests.get(GOOGLEMAP_URL, params={'query': query})
if response.status_code == 200:
    result = response.json()
    latitude = result['latitude']
    longitude = result['longitude']
else:
    error = response.json().get('error', 'Location not found')

```
#Running the Microservice Locally
1. Start the Server
```
Python googlemap.py
```
2. Start the Flask App
```
Python app.py
```
3. Start the generate_map html
#Example of rendering the map with Flask
```
 <script>
            window.onload = function() {
                initMap(); 
            };

            function initMap() {
                var location = { lat: {{ latitude }}, lng: {{ longitude }} };

                var map = new google.maps.Map(document.getElementById("map"), {
                    zoom: 15,
                    center: location
                });

                var marker = new google.maps.Marker({
                    position: location,
                    map: map
                });
            }
        </script>

```
4. Diagram

![api_microservice_aa](https://github.com/user-attachments/assets/3bc157a7-4aaa-49dd-b0b3-960b2b4ab72b)
