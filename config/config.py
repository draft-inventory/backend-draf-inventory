import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql://root:sMLSunOqcDvKKhXKkjkxAjtdmjUmwnds@autorack.proxy.rlwy.net/railway')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'secret_key')
