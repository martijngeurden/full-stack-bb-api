from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import models.bp_model
# files from Martijn Geurden
from queries import mag_queries
from models import mag_models

# files from Brecht Proesmans
from queries import bp_queries
from models import bp_model

import config
import database

app = FastAPI(docs_url=config.documentation_url)

origins = config.cors_origins.split(",")

app.add_middleware(
    CORSMiddleware,
    # todo: aan te passen na hosting
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/get/subs")
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


@app.post("/post/sub")
def create_sub(sub: mag_models.model_subscription):
    query = mag_queries.sub_push
    mailToCheck = mag_queries.sub_check_mail
    mailingList = database.execute_sql_query(mailToCheck)
    for i in range(len(mailingList)):
        if mailingList[i][0] == sub.email:
            return 'Failed : "' + sub.email + '" already exists', 418
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
    if isinstance(sub, Exception):
        return "Error reaching the DataBase, please try again later", 500


@app.get("/get/pastries")
def get_pastries(rating: int = 0, order: int = 0):
    if order == 1:
        query = mag_queries.pastries
    else:
        query = mag_queries.pastriesDesc

    pastries = database.execute_sql_query(query, (
        rating,
    ))
    if isinstance(pastries, Exception):
        return pastries, 500
    all_pastries_to_return = []
    for pastry in pastries:
        all_pastries_to_return.append({
            "productID": pastry[0],
            "productName": pastry[1],
            "shortDescription": pastry[2],
            "longDescription": pastry[3],
            "imageLocation": pastry[4],
            "videoLocation": pastry[5],
            "price": pastry[6],
            "score": pastry[7]
        })
    return {'data': all_pastries_to_return}


# De code hieronder is door Brecht Proesmans getypt op de laptop van Martijn Geurden omdat mijn laptop te oud is om
# pycharm deftig te runnen, hij herkent momenteel het pip-commando zelfs niet. Vince is hier in de klas ook getuige
# van geweest. Vandaar werk ik op de laptop van Martijn hiervoor.
@app.get("/review")
def reviews():
    query = bp_queries.all_reviews
    reviews = database.execute_sql_query(query)
    if isinstance(reviews, Exception):
        return reviews, 500
    reviews_to_return = []
    for review in reviews:
        reviews_to_return.append({
            "title": review[1],
            "content": review[2],
            "author": review[3],
        })
    return {'Reviews': reviews_to_return}


@app.post("/applicants")
def applicants(applicant: bp_model.Applicants):
    query = bp_queries.apply
    success = database.execute_sql_query(query, (
        applicant.mail,
        applicant.name,
        applicant.motivation,
    ))
    if isinstance(success, Exception):
        return success, 500
    if success:
        return applicant

@app.get("/people")
def people(gender: str = ""):
    query = bp_queries.people
    people = database.execute_sql_query(query, (
        '%{}%'.format(gender),
    ))
    people_to_return = []
    for peop in people:
        people_to_return.append({
            "name": peop[1],
            "shortDescription": peop[2],
            "longDescription": peop[3],
            "gender": peop[4],
        })
    return {'People': people_to_return}
