from pydantic import BaseModel, Field
from datetime import datetime

class objava(BaseModel):
    id: int
    korisnik: str = Field(max_length=20)
    tekst: str = Field(max_length=280)
    vrijeme: datetime


class addObjava(BaseModel):
    korisnik: str = Field(max_length=20)
    tekst: str = Field(max_length=280)
    vrijeme: datetime
