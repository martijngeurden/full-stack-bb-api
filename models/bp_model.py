from pydantic import BaseModel

class Applicants(BaseModel):
    mail: str
    name: str
    motivation: str

