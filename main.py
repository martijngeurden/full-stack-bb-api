from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#files from Martijn Geurden
from queries import mag_queries
from models import mag_models

#files from XXXXXX


import config
import database

app = FastAPI(docs_url=config.documentation_url)

origins = config.cors_origins.split(",")


app.add_middleware(
    CORSMiddleware,
    #todo: aan te passen na hosting
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/subs")
def get_all_subs():
    query = mag_queries.sub_all
    all_subs = database.execute_sql_query(query)
    if isinstance(all_subs, Exception):
        return all_subs, 500
    all_subs_to_return = []
    for sub in all_subs:
        all_subs_to_return.append({
            "email": sub[0],
            "firstName": sub[1],
            "lastName": sub[2],
            "subscriptionType": sub[3],
            "address": sub[4],
            "address2": sub[5],
            "zipCode": sub[6],
            "city": sub[7],
            "additionalInformation": sub[8]
        })
    return {'subscriptions': all_subs_to_return}


@app.post("/subpost")
def create_sub(sub: mag_models.model_subscription):
    query = mag_queries.sub_push
    success = database.execute_sql_query(query, (
        sub.email,
        sub.firstName,
        sub.lastName,
        sub.subscriptionType,
        sub.address,
        sub.address2,
        sub.zipCode,
        sub.city,
        sub.additionalInformation,
    ))
    if success:
        return sub

@app.get("/get/pastries")
def get_all_subs():
    query = mag_queries.pastries_all
    all_pastries = database.execute_sql_query(query)
    if isinstance(all_pastries, Exception):
        return all_pastries, 500
    all_pastries_to_return = []
    for pastry in all_pastries:
        all_pastries_to_return.append({
            "productName": pastry[1],
            "shortName": pastry[2],
            "longDescription": pastry[3],
            "imageLocation": pastry[4],
            "videoLocation": pastry[5]
        })
    return {'pastries': all_pastries_to_return}
