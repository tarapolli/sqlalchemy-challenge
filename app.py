# Import Flask, SQL toolkit, Objetct Relational Mappy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# create engine to hawaii.sqlite
engine = create_engine("sqlite:///hawaii.sqlite")

# declare base and use base class to reflect db tables
Base = automap_base()
Base.prepare(engine, reflect=True)

# Print all of the classes mapped to the Base
Base.classes.keys()

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)

# Create an app
app = Flask(__name__)

# Home page.
# List all routes that are available.

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs"
    )


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
    # Create our session (link) from Python to the DB
    session = Session(engine)
    # query
    results = session.query(Measurement.prcp).all()

    session.close()

    # Convert list of tuples into normal list
    all_prcp = list(np.ravel(results))
    # Return a JSON list of stations from the dataset.
    return jsonify(all_prcp)


# station route
@app.route("/api/v1.0/stations")
def station_route():
    return (session.query(Station.station).count()
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

# @app.route("/api/v1.0/<start>/<end")
# def end_date_route():



# the end.
if __name__ == "__main__":
    app.run(debug=True)
