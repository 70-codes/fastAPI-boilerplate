from database import Base
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    fname = Column(String)
    lname = Column(String)
    email = Column(String, index=True)
    password = Column(String)
    created_at = Column(String)
