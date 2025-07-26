from fastapi import FastAPI , Depends
from database import Base , SessionLocal, create_engine
from model import User
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List

Base.metadata.create_all(bind=create_engine)


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class UserSchema(BaseModel):
   
    name : str
    email: str
    password: str

    class Config:
        orm_mode = True

class UserList(BaseModel):
    id: int
    name : str
    email: str

    class Config:
        orm_mode = True



@app.post("/users")
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    db_user = User(name=user.name,email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users" , response_model=List[UserList])
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@app.get("/users/{user_id}", response_model=UserList)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    return user


@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserSchema, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    db_user.name = user.name
    db_user.email = user.email
    db.commit()
    db.refresh(db_user)
    return db_user  

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}