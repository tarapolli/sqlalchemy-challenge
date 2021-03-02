# Import Flask
from flask import Flask, jsonify

# Create an app
app = Flask(__name__)

query_results_dict = {"date": "prcp"}

# Home page.
# List all routes that are available.

# API STATIC ROUTES
@app.route("/")
def home():
    print("Server received rquest for 'Home' page...")
    return "Welcome to the Hawaii Climate App page!"

# convert query results to a dictionary using date as the key and prcp as the value.
# Return the JSON representation of your dictionary.
# precipiation route
@app.route("/api/v1.0/precipitation")
def precipiation_route():


    return jsonify(precipiation_route)


# Return a JSON list of stations from the dataset.
# station route
@app.route("/api/v1.0/stations")
def station_route():
    return (NumberStations = session.query(Station.station).count()
        f"Welcome to the Justice League API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/justice-league"
    )

# Query dates & temp observations of the most active station for the last year of data.
# Return a JSON list of temperature observations (TOBS) for the previous year.
# temperature route
@app.route("/api/v1.0/tobs")
def temp_route():

# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
# When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
# API DYNAMIC ROUTE
@app.route("/api/v1.0/<start>")
def start_date_route():

@app.route("/api/v1.0/<start>/<end")
def end_date_route():



# the end.
if __name__ == "__main__":
    app.run(debug=True)
