from fastapi import FastAPI

import config
import database
from queries import festival_queries as queries
from queries import coaster_queries as queries


app = FastAPI(docs_url=config.documentation_url)


@app.get("/festivals")
def get_all_festivals():
    query = queries.festival_name_query
    festivals = database.execute_sql_query(query)
    if isinstance(festivals, Exception):
        return festivals, 500
    festivals_to_return = []
    for festival in festivals:
        festivals_to_return.append(festival[0])
    return {'festivals': festivals_to_return}

@app.get("/themeparks")
def get_all_themeparks():
    query = queries.themepark_query
    themeparks = database.execute_sql_query(query)
    if isinstance(themeparks, Exception):
        return themeparks, 500
    themeparks_to_return = []
    for themepark in themeparks:
        themeparks_to_return.append(themepark[0])
    return {'themeparks': themeparks_to_return}

@app.get("/themeparks/detail")
def get_all_parkDetails():
    query = queries.parkDetails
    parkDetails = database.execute_sql_query(query)
    if isinstance(parkDetails, Exception):
        return parkDetails, 500
    parkDetails_to_return = []
    for detail in parkDetails:
        parkDetails_to_return.append({"name": detail[0], "openingDate": detail[1], "city": detail[2], "website": detail[3]})
    return {'themeparks': parkDetails_to_return}

@app.get("/themeparks/opening")
def get_opening_info(year: int):
    query = queries.parkOpening
    parkOpenings = database.execute_sql_query(query, (
        year,
    ))
    if isinstance(parkOpenings, Exception):
        return parkOpenings, 500
    parkOpenings_to_return = []
    for opening in parkOpenings:
        parkOpenings_to_return.append({"name": opening[0], "openingDate": opening[1], "city": opening[2], "website": opening[3]})
    return {'themeparks': parkOpenings_to_return}


@app.get("/themeparks/inversions")
def get_inversions(number: int = 1):
    query = queries.inversions
    inversions = database.execute_sql_query(query, (
        number,
    ))
    if isinstance(inversions, Exception):
        return inversions, 500
    inversions_to_return = []
    for inversion in inversions:
        inversions_to_return.append({"name": inversion[0], "length": inversion[1], "height": inversion[2],
                                     "maximumSpeed": inversion[3], "inversions": inversion[4]})
    return {'themeparks': inversions_to_return}


@app.get("/coasters")
def get_coasters(coasterID: int):
    query = queries.coasters
    coasters = database.execute_sql_query(query, (
        coasterID,
    ))
    if isinstance(coasters, Exception):
        return coasters, 500
    coasters_to_return = []
    for inversion in coasters:
        coasters_to_return.append({"name": inversion[0], "length": inversion[1], "height": inversion[2],
                                     "maximumSpeed": inversion[3], "inversions": inversion[4]})
    if coasters_to_return == []:
        return {}
    else:
        return {'themeparks': coasters_to_return}

