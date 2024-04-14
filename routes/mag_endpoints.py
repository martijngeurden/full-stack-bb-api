# mag = Martijn Geurden

from fastapi import APIRouter
import database
from queries import mag_queries
from models import mag_models

app = APIRouter()


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


@app.post("/post/order")
def order(order: mag_models.model_order):
    query = mag_queries.post_order
    success = database.execute_sql_query(query, (
        order.name,
        order.date,
        order.details,
    ))
    if isinstance(success, Exception):
        return success, 500
    if success:
        return order

