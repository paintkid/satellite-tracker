# Imports
from flask import Flask
from flask_cors import CORS
from skyfield.api import load

# Initialize Flask
app = Flask(__name__)
# Allow frontend requests to backend
CORS(app)

# Skyfield Timescale setup
ts = load.timescale()

# Active satellites from Celestrak (TLE format)
satellites_info_url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle"

satellites = load.tle_file(satellites_info_url)
by_name = {sat.name: sat for sat in satellites}
iss = by_name.get('ISS (ZARYA)')

if __name__ == "__main__":
    t = ts.now()
    position = iss.at(t)
    x, y, z = position.position.km
    print(f"Position of ISS:\n  x: {x:.2f} km\n  y: {y:.2f} km\n  z: {z:.2f} km")

    app.run()


