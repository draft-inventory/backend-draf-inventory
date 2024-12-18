from ...infrastructure.repositories.user_repository import UserRepository
from werkzeug.security import generate_password_hash, check_password_hash


class UserService:
    @staticmethod
    def register_user(name, last_name, email, user_name, password):
        # Validar unicidad de usuario y correo
        if UserRepository.find_by_username(user_name):
            raise ValueError("El nombre de usuario ya está en uso")
        if UserRepository.find_by_email(email):
            raise ValueError("El correo ya está registrado")

        # Hash de la contraseña
        hashed_password = generate_password_hash(password)
        user_data = {
            "name": name,
            "last_name": last_name,
            "email": email,
            "user_name": user_name,
            "password": hashed_password
        }
        return UserRepository.create_user(user_data)

    @staticmethod
    def login_user(user_name, password):
        # Buscar usuario por user_name
        user = UserRepository.find_by_username(user_name)
        if not user or not check_password_hash(user.password, password):
            raise ValueError("Nombre de usuario o contraseña incorrectos")
        return user
