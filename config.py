import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    MYSQL_HOST = os.getenv('DB_HOST')
    MYSQL_USER = os.getenv('DB_USER')
    MYSQL_PASSWORD = os.getenv('DB_PASSWORD')
    MYSQL_DB = os.getenv('DB_NAME')
