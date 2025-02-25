import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "MyKey")
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/flaskapp")
    MAIL_SERVER = 'smtp.example.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv("MAIL_USERNAME", "your_email@example.com")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", "your_email_password")