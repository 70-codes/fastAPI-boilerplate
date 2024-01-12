from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import User
from schemas.schemas import BaseUser, ShowUser
from . import create_route
from typing import List
from repository import user_repo


router = create_route(prefix="user", tags="Users")


@router.post("")
async def create_user(
    request: BaseUser,
    db: Session = Depends(get_db),
):
    return user_repo.create_user(
        request=request,
        db=db,
    )
    pass


@router.get(
    "",
    response_model=List[ShowUser],
)
async def root(db: Session = Depends(get_db)):
    return user_repo.get_users(db=db)


@router.get("/{id}")
async def get_user_by_id(
    id: int,
    db: Session = Depends(get_db),
):
    return user_repo.get_user_by_id(id=id, db=db)
    pass


@router.put(
    "/{id}",
    response_model=ShowUser,
)
async def update_user(
    request: BaseUser,
    id: int,
    db: Session = Depends(get_db),
):
    return user_repo.update_user(id=id, request=request, db=db)
    pass


@router.delete("/{id}")
async def delete_user(
    id: int,
    db: Session = Depends(get_db),
):
    return user_repo.delete_user(id=id, db=db)
    pass
