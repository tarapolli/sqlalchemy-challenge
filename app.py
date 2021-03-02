# 1. Import Flask
from flask import Flask


# 2. Create an app
app = Flask(__name__)


# 3. Define static routes
@app.route("/")
def index():
    return "Hawaii Climate App"


@app.route("/api/v1.0/precipitation")
def precipiation_route():
    """Return the justice league data as json"""

    return jsonify(justice_league_members)


@app.route("/api/v1.0/stations")
def station_route():
    return (
        f"Welcome to the Justice League API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/justice-league"
    )


@app.route("/api/v1.0/tobs")
def temp_route():

@app.route("/api/v1.0/<start>")
def start_date_route():

@app.route("/api/v1.0/<start>/<end")
def end_date_route():