from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt

mongo = PyMongo()
bcrypt = Bcrypt()

class User:
    @staticmethod
    def register_user(email, password):
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        return mongo.db.users.insert_one({"email": email, "password": hashed_password})
    
    @staticmethod
    def find_by_email(email):
        return mongo.db.users.find_one({"email": email})
    
    @staticmethod
    def update_password(email, new_password):
        hashed_password = bcrypt.generate_password_hash(new_password).decode("utf-8")
        return mongo.db.users.update_one({"email": email}, {"$set": {"password": hashed_password}})