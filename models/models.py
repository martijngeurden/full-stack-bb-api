from pydantic import BaseModel


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
