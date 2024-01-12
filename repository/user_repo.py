from models import User
from fastapi import status, HTTPException
from datetime import datetime
import hash


def get_users(db):
    return db.query(User).all()
    pass


def get_user_by_email(db, request):
    email = request.email
    user = db.query(User).filter(User.email == email).first()
    return user
    pass


def create_user(request, db):
    user = get_user_by_email(db=db, request=request)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this email already exists",
        )

    else:
        hashed_password = hash.get_password_hash(request.password)
        new_user = User(
            fname=request.fname,
            lname=request.lname,
            email=request.email,
            password=hashed_password,
            created_at=datetime.utcnow(),
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    pass


def get_user_by_id(db, id):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found",
        )
    return user
    pass


def update_user(db, id, request):
    user = db.query(User).filter(User.id == id).first()
    email = get_user_by_email(db, request.email)
    if email:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this email already exists",
        )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist",
        )

    user.fname = request.fname
    user.lname = request.lname
    user.email = request.email

    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def delete_user(id, db):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found",
        )
    db.delete(user)
    db.commit()
    return {
        "message": "User deleted successfully",
    }
    pass
