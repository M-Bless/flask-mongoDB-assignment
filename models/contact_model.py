from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt

mongo = PyMongo()
bcrypt = Bcrypt()


class Contact:
    @staticmethod
    def add_contact(data):
        return mongo.db.contacts.insert_one(data)
    
    @staticmethod
    def find_by_registration_number(registration_number):
        return mongo.db.contacts.find_one({"registration_number": registration_number})