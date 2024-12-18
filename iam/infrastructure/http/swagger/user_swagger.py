from flasgger import swag_from

# register_user_swagger
register_user_swagger = {
    "tags": ["User"],
    "summary": "Register a new user",
    "description": "Create a new user by providing necessary details such as name, last name, email, user_name, and password.",
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "First name of the user."
                    },
                    "last_name": {
                        "type": "string",
                        "description": "Last name of the user."
                    },
                    "email": {
                        "type": "string",
                        "description": "Email address. Must be unique."
                    },
                    "user_name": {
                        "type": "string",
                        "description": "Unique user name. Must be 5-20 characters, no spaces or special characters."
                    },
                    "password": {
                        "type": "string",
                        "description": "User password. Must be at least 8 characters, include one uppercase letter, one lowercase letter, one number, and one special character."
                    }
                },
                "required": ["name", "last_name", "email", "user_name", "password"]
            }
        }
    ],
    "responses": {
        201: {
            "description": "User registered successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "description": "User ID"
                    },
                    "name": {
                        "type": "string",
                        "description": "First name of the user"
                    },
                    "last_name": {
                        "type": "string",
                        "description": "Last name of the user"
                    },
                    "email": {
                        "type": "string",
                        "description": "Email address of the user"
                    },
                    "user_name": {
                        "type": "string",
                        "description": "Unique username"
                    }
                }
            }
        },
        400: {
            "description": "Invalid input or user already exists",
            "schema": {
                "type": "object",
                "properties": {
                    "error": {
                        "type": "string",
                        "description": "Error message"
                    }
                }
            }
        },
        500: {
            "description": "Internal server error",
            "schema": {
                "type": "object",
                "properties": {
                    "error": {
                        "type": "string",
                        "description": "Error message"
                    },
                    "except": {
                        "type": "string",
                        "description": "Exception details"
                    }
                }
            }
        }
    }
}


# login_user_swagger
login_user_swagger = {
    "tags": ["User"],
    "summary": "User login",
    "description": "Authenticate a user using their username and password.",
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "user_name": {
                        "type": "string",
                        "description": "Unique username."
                    },
                    "password": {
                        "type": "string",
                        "description": "User password."
                    }
                },
                "required": ["user_name", "password"]
            }
        }
    ],
    "responses": {
        200: {
            "description": "Login successful",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "description": "User ID"
                    },
                    "name": {
                        "type": "string",
                        "description": "First name of the user"
                    },
                    "last_name": {
                        "type": "string",
                        "description": "Last name of the user"
                    },
                    "email": {
                        "type": "string",
                        "description": "Email address of the user"
                    },
                    "user_name": {
                        "type": "string",
                        "description": "Unique username"
                    }
                }
            }
        },
        400: {
            "description": "Invalid username or password",
            "schema": {
                "type": "object",
                "properties": {
                    "error": {
                        "type": "string",
                        "description": "Error message"
                    }
                }
            }
        },
        500: {
            "description": "Internal server error",
            "schema": {
                "type": "object",
                "properties": {
                    "error": {
                        "type": "string",
                        "description": "Error message"
                    },
                    "except": {
                        "type": "string",
                        "description": "Exception details"
                    }
                }
            }
        }
    }
}
