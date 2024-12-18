from flask import Blueprint, request, jsonify
from flasgger import swag_from
from ...application.services.user_service import UserService
from ...domain.schemas.user_schema import user_register_schema, user_login_schema, user_schema
from ...infrastructure.http.swagger.user_swagger import register_user_swagger, login_user_swagger

user_urls = Blueprint('user_blueprint', __name__)

@user_urls.route('/register', methods=['POST'])
@swag_from(register_user_swagger)
def register():
    try:
        # Validar y cargar datos del esquema
        data = user_register_schema.load(request.get_json())
        user = UserService.register_user(
            name=data['name'],
            last_name=data['last_name'],
            email=data['email'],
            user_name=data['user_name'],
            password=data['password']
        )
        return jsonify(user_schema.dump(user)), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Error en el servidor"}), 500

@user_urls.route('/login', methods=['POST'])
@swag_from(login_user_swagger)
def login():
    try:
        # Validar y cargar datos del esquema
        data = user_login_schema.load(request.get_json())
        user = UserService.login_user(
            user_name=data['user_name'],
            password=data['password']
        )
        return jsonify(user_schema.dump(user)), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Error en el servidor"}), 500