from common.db.db import ma
from ...domain.models.user import User


# Esquema para serialización general
class UserSchema(ma.Schema):
    class Meta:
        model = User
        fields = (
            "id",
            "name",
            "last_name",
            "email",
            "user_name"
        )


# Esquema para el registro de usuarios
class UserRegisterSchema(ma.Schema):
    class Meta:
        fields = (
            "name",
            "last_name",
            "email",
            "user_name",
            "password"
        )


# Esquema para el login
class UserLoginSchema(ma.Schema):
    class Meta:
        fields = (
            "user_name",
            "password"
        )


# Instancias de esquemas
user_schema = UserSchema()
user_register_schema = UserRegisterSchema()
user_login_schema = UserLoginSchema()
