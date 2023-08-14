from skyfield.api import load, Topos

# Load satellite TLE data
stations_url = 'http://celestrak.com/NORAD/elements/stations.txt'
satellites = load.tle_file(stations_url)

# Get the TLE data for the International Space Station (ISS)
iss = satellites['ISS (ZARYA)']

# Create an observer (location)
latitude = 0.0  # Change this to your desired latitude
longitude = 0.0  # Change this to your desired longitude
elevation = 0.0  # Change this to your desired elevation (meters)
observer = Topos(latitude_degrees=latitude, longitude_degrees=longitude, elevation_m=elevation)

# Get the position of the ISS at a specific time
ts = load.timescale()
t = ts.now()  # Current time

geocentric = iss.at(t)
subpoint = geocentric.subpoint()

print(f"Time: {t.utc_iso()}")
print(f"Latitude: {subpoint.latitude.degrees:.6f}°")
print(f"Longitude: {subpoint.longitude.degrees:.6f}°")
print(f"Altitude: {subpoint.elevation.km:.2f} km")

