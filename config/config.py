import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:sMLSunOqcDvKKhXKkjkxAjtdmjUmwnds@autorack.proxy.rlwy.net:15545/railway'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'secret_key')
