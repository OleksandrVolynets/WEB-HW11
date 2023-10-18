from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr



class ContactBase(BaseModel):
    id: int
    firstname: str = Field(max_length=100)
    lastname: str = Field(max_length=100)
    email: str = Field(max_length=150)
    phonenumber: str = Field(max_length=20)
    birthday: date
    description: str = Field(max_length=1500)


class ContactResponse(ContactBase):
    id: int
    firstname: str
    lastname: str
    email: EmailStr
    phonenumber: str
    birthday: date
    description: str

    class Config:
        orm_mode = True