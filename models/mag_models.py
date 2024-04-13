from pydantic import BaseModel
from datetime import date


class model_subscription(BaseModel):
    email: str
    firstName: str
    lastName: str
    subscriptionType: str
    address: str
    address2: str = None
    zipCode: int
    city: str
    additionalInformation: str = None


class model_order(BaseModel):
    name: str
    date: date
    details: str