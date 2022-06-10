from fastapi import APIRouter
from config.db import conn
from models.user import users
from schemas.user import User
from cryptography.fernet import Fernet

key = Fernet.generate_key()
fPass = Fernet(key)

user = APIRouter()

@user.get("/users")
def get_users():
    return conn.execute(users.select()).fetchall()

@user.post("/users")
def get_users(user: User):
    new_user = {"name": user.name, "email": user.email, "password": fPass.encrypt(user.password.encode('utf-8'))}
    result = conn.execute(users.insert().values(new_user))
    print(result.lastrowid)
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()

@user.get("/users/{id}")
def get_users(id: str):
    return conn.execute(users.select().where(users.c.id == id)).first()