from flask import Flask, request, jsonify
import csv
app = Flask(__name__)

ufo_sightings = [
    {
        "datetime": "10/10/1949 20:30",
        "city": "san marcos",
        "state": "tx",
        "country": "us",
        "shape": "cylinder",
        "duration (seconds)": "2700",
        "duration (hours/min)": "45 minutes",
        "comments": "This event took place in early fall around 1949-50. It occurred after a Boy Scout meeting in the Baptist Church. The Baptist Church sit",
        "date posted": "4/27/2004",
        "latitude": "29.8830556",
        "longitude": "-97.9411111"
    },
    {
        "datetime": "10/10/1949 21:00",
        "city": "lackland afb",
        "state": "tx",
        "country": "",
        "shape": "light",
        "duration (seconds)": "7200",
        "duration (hours/min)": "1-2 hrs",
        "comments": "1949 Lackland AFB&#44 TX.  Lights racing across the sky &amp; making 90 degree turns on a dime.",
        "date posted": "12/16/2005",
        "latitude": "29.38421",
        "longitude": "-98.581082"
    }
]

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>UFO Sightings</title>
        </head>
        <body>
            <h1>Welcome to the UFO Sightings API</h1>
            <p>Use the /sightings route to get UFO sighting data.</p>
        </body>
    </html>
    """

@app.route('/sightings', methods=['GET'])
def get_sightings():
    country = request.args.get('country', '')
    scrubbed_sightings = load_ufo_data('scrubbed.csv')
    return jsonify(scrubbed_sightings)
    
def load_ufo_data(filepath):
    sightings = []
    with open(filepath, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            sightings.append(row)
    return sightings

@app.route('/top_ten', methods=['GET'])  
def top_ten():
    sightings = load_ufo_data('scrubbed.csv')[:10]
    html_string = ""
    for sighting in sightings:
        html_string += f"<p>Location: {sighting["city"]}, {sighting["state"]}, {sighting["country"]}. Date: {sighting["date posted"]}</p>"

    return f"""
    <html>
        <head>
            <title>Top Ten UFO Sightings</title>
        </head>
        <body>
            <h1>Top Ten Sightings</h1>
            {html_string}
        </body>
    </html>
    """

@app.route('/research_stations', methods=['GET'])
def get_research_stations():
    stations = []
    with open('research_stations.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            stations.append(row)
    return jsonify(stations)

@app.route('/add_research_station', methods=['POST'])
def add_research_station():
    data = request.get_json()
    name = data.get('name')
    location = data.get('location')
    if not name or not location:
        # the second parameter is status code 400 for bad request
        return jsonify({'error': 'Name and location are required'}), 400
    # below we append the new research station to the CSV file
    with open('research_stations.csv', mode='a', newline='') as file:
        fieldnames = ['name', 'location']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({'name': name, 'location': location})
    return jsonify({'message': 'Research station added successfully'}), 201