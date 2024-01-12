import models
from database import engine


def create_db():
    return models.Base.metadata.create_all(bind=engine)
