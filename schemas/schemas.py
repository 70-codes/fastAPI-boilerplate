from pydantic import BaseModel
from typing import List


class BaseUser(BaseModel):
    fname: str
    lname: str
    email: str
    password: str
    created_at: str


class ShowUser(BaseUser):
    id: int

    class Config:
        orm_mode = True
