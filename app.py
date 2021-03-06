# Import Flask, SQL toolkit, Objetct Relational Mappy
import datetime as dt
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# create engine to hawaii.sqlite
engine = create_engine("sqlite:///hawaii.sqlite") #connect_args=('check_same_thread'L False

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
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;<br>"
	)
    
# API STATIC ROUTES
@app.route("/")
def home():
    print("Server received rquest for 'Home' page...")
    return "Welcome to the Hawaii Climate App page!"


# precipiation route
@app.route("/api/v1.0/precipitation")
def precipiation_route():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # convert query results to a dictionary using date as the key and prcp as the value.
    # calculate the date one year from the last date in data set
    recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    one_year_prior = (dt.datetime.strptime(recent_date[0],'%Y-%m-%d') - dt.timedelta(days=364)).strftime('%Y-%m-%d')
    # query to retrieve the last 12 months of precipitation data
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_prior).all()
    # Convert list of tuples into normal list
    # all_prcp = {result[0]:result[1] for result in results}  
    all_prcp = {date:prcp for date, prcp in results}  
    # Return the JSON representation of your dictionary.
    return jsonify(precipitation = all_prcp)

    session.close()


# station route
@app.route("/api/v1.0/stations")
def station_route():
     # Create our session (link) from Python to the DB
    session = Session(engine)

    results = session.query(Station.station).all()
    # Convert list of tuples into normal list
    StationList = list(np.ravel(results))
    # Return a JSON list of stations from the dataset
    return jsonify(stations = StationList)

    session.close()

# temperature route
@app.route("/api/v1.0/tobs")
def temp_route():
 # Create our session (link) from Python to the DB
    session = Session(engine)
   
    # Query dates & temp observations of the most active station for the last year of data.
    results = session.query(Measurement.station, Measurement.date, Measurement.tobs).\
        filter(Measurement.station == "USC00519281").\
        filter(Measurement.date >= "2016-08-24", Measurement.date <= "2017-08-23").all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_temps
    all_temps = []
    for station, date, temp in results:
        temp_dict = {}
        temp_dict["station"] = station
        temp_dict["date"] = date
        temp_dict["temp"] = temp
        all_temps.append(temp_dict)

    # Return a JSON list of temperature observations (TOBS) for the previous year.
    return jsonify(all_temps)


# API DYNAMIC ROUTE
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def stats(start, end = None):
    session = Session(engine)
    # return a JSON of min, max, avg temp for a user-defined start date; end date not req'd 
    if not end:
        results = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
            filter(Measurement.date >= start).all()
    else:
        results = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
            filter(Measurement.date >= start).filter(Measurement.date < end).all()
    final_results = list(np.ravel(results))
    
    # Return JSON List of Min Temp, Avg Temp and Max Temp for a Given Start Range
    return jsonify(temps = final_results)

    session.close()


# the end.
if __name__ == "__main__":
    app.run(debug=True)
