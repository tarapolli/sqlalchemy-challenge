
SQLAlchemy Homework - Surfs Up!

About this project:  
This project does a deep-dive into the Hawaiian climate as an integral part of vacation planning. I used Python and SQLAlchemy to do basic climate analysis and data exploration of my climate database, using SQLAlchemy ORM queries, Pandas, and Matplotlib. See below for the three components of this project.

PRECIPIATION ANALYSIS
Idenified the most recent date in the data set.
Using this date, I retrieve the last 12 months of precipitation data by querying the 12 preceding months of data. 
Select only the date and precipitation values.
Load the query results into a Pandas DataFrame and set the index to the date column.
Sort the DataFrame values by date.
Plot the results using the DataFrame plot method.
Print its summary statistics.

STATION ANALYSIS
Design a query to calculate the total number of stations in the dataset.
Design a query to find the most active stations.
List the stations and observation counts in descending order.
Identify which station id has the highest number of observations?
Using the most active station id, calculate the lowest, highest, and average temperature.
Design a query to retrieve the last 12 months of temperature observation data (TOBS).
Filter by the station with the highest number of observations.
Query the last 12 months of temperature observation data for this station.
Plot the results as a histogram.

DESIGN A FLASK API
Create the following routes:
 * Home /
 * Precipiation /api/v1.0/precipitation
 * Stations /api/v1.0/stations
 * Temperatures for 12 months at most active station  /api/v1.0/tobs
 * Minimum, Maximum, Average temperatures for user-defined start and end dates  /api/v1.0/<start> and /api/v1.0/<start>/<end>



