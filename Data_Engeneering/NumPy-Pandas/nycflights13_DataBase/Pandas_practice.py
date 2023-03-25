import pandas as pd
import numpy as np

airlines = pd.read_csv('https://raw.githubusercontent.com/tidyverse/nycflights13/main/data-raw/airports.csv')

airports = pd.read_csv('https://raw.githubusercontent.com/tidyverse/nycflights13/main/data-raw/airports.csv')

planes = pd.read_csv('https://raw.githubusercontent.com/tidyverse/nycflights13/main/data-raw/planes.csv')

weather = pd.read_csv('https://raw.githubusercontent.com/tidyverse/nycflights13/main/data-raw/weather.csv')

flights = pd.read_csv('https://raw.githubusercontent.com/vaibhavwalvekar/NYC-Flights-2013-Dataset-Analysis/master/flights.csv')



#print(airlines.columns)
#print(airports.columns)
print(planes.columns)
#print(weather.columns)
print(flights.columns)
#print(airlines.info())
#print(airports.info())
#print(planes.info())
#print(weather.info())
#print(flights.sample(10))

# 0. In the flights table from the nycflights13 database, select all columns between year and day
# (inclusive), without referring to column numbers explicitly (the code should work if we randomly
# rearrange the columns too). Then select all columns except those between year and day (inclusive).

"""if flights.columns.get_loc("year") <= flights.columns.get_loc("day"):
    included = flights.loc[:, "year":"day"]
    excluded = flights.loc[:, :"year"].concat(column for column in flights.loc[:, "day":].columns if column != "day")
else: 
    included = flights.loc[:, "day":"year"]
    excluded = flights.loc[:, :"day"].concat(column for column in flights.loc[:, "year":].columns if column != "year")
print(included, excluded)"""

# 1. SELECT DISTINCT engine FROM planes

"""result1 = planes.engine.unique()
print(result1)"""

# 2. SELECT DISTINCT type, engine FROM planes

"""type_and_engine_count = planes.groupby(["type", "engine"]).engine.count()
result2 = planes.groupby(["type"]).engine.unique()
print(type_and_engine_count, result2)"""

# 3. SELECT COUNT(*), engine FROM planes GROUP BY engine

"""result3 = planes.groupby("engine").engine.count()
print(result3)"""

# 4. SELECT COUNT(*), engine, type FROM planes GROUP BY engine, type

"""result4 = planes.groupby(["type", "engine"]).engine.count()
print(result4)"""

# 5. SELECT MIN(year), AVG(year), MAX(year), engine, manufacturer FROM planes GROUP BY engine, manufacturer
 
"""result5 = planes.groupby(["engine", "manufacturer"]).year.agg([min(), np.mean(), max()])
print(result5)"""

# 6. SELECT * FROM planes WHERE speed IS NOT NULL

"""result6 = planes.loc[planes.speed.notna()]
print(result6)"""

# 7. SELECT tailnum FROM planes WHERE seats BETWEEN 150 AND 190 AND year >= 2012

"""result7 = planes["tailnum"].loc[(planes["seats"] >= 150) & (planes["seats"] < 190) & (planes["year"] >= 1012)]
print(result7)"""

# 8. SELECT * FROM planes WHERE manufacturer IN ("BOEING", "AIRBUS", "EMBRAER") AND seats > 390

"""result8 = planes.loc[(planes.manufacturer.isin(["BOEING", "AIRBUS", "EMBRAER"])) & (planes.seats > 390)]
print(result8)"""

# 9. SELECT DISTINCT year, seats FROM planes WHERE year >= 2012 ORDER BY year ASC, seats DESC

"""result9 = planes[planes.year >= 2012].loc[:, ['year', "seats"]].drop_duplicates()
result9 = result9.sort_values(by= ['year', "seats"], ascending= [True, False])
print(result9)"""

# 10. SELECT DISTINCT year, seats FROM planes WHERE year >= 2012 ORDER BY seats DESC, year ASC

"""result10 = planes[planes.year >= 2012].loc[:, ['seats', "year"]].drop_duplicates().sort_values(by= ["seats", 'year'], ascending= [False, True])
print(result10)"""

# 11. SELECT manufacturer, COUNT(*) FROM planes WHERE seats > 200 GROUP BY manufacturer

"""result11 = planes[planes.seats > 200].groupby("manufacturer").size()
print(result11)"""

# 12. SELECT manufacturer, COUNT(*) FROM planes GROUP BY manufacturer HAVING COUNT(*) > 10

"""result12 = planes.groupby("manufacturer").size()
result12 = result12.loc[result12 > 10]
print(result12)"""

# 13. SELECT manufacturer, COUNT(*) FROM planes WHERE seats > 200 GROUP BY manufacturer HAVING COUNT(*) > 10

"""result13 = planes[planes["seats"] > 200].groupby("manufacturer").size()
result13 = result13.loc[result13 > 10]
print(result13)"""

# 14. SELECT manufacturer, COUNT(*) AS howmany FROM planes GROUP BY manufacturer ORDER BY howmany DESC LIMIT 5

"""result14 = planes.groupby("manufacturer").size().reset_index(name="howmany").sort_values("howmany", ascending= False).head(5)
print(result14)"""

# 15. SELECT * FROM flights LEFT JOIN planes ON flights.tailnum=planes.tailnum

"""result15 = pd.merge(flights, planes, on='tailnum', how='left').set_index("Unnamed: 0").reset_index(drop= True).rename(columns= {"year_x": "flight_year", "year_y": "plane_year"})
print(result15)"""



