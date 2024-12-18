from ...domain.models.user import User
from common.db.db import db

class UserRepository:
    @staticmethod
    def find_by_username(user_name):
        return User.query.filter_by(user_name=user_name).first()

    @staticmethod
    def find_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def create_user(user_data):
        new_user = User(**user_data)
        db.session.add(new_user)
        db.session.commit()
        return new_user
