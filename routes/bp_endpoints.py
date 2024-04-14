# bp = Brecht Proesmans

from fastapi import APIRouter
import database
from queries import bp_queries
from models import bp_model

app = APIRouter()

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
