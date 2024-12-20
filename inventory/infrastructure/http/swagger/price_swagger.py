from flasgger import swag_from

# Create_price_swagger
create_price_swagger = {
    "tags": ["Price"],
    "summary": "Create a new price",
    "description": "Create a new price",
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "cost_price": {
                        "type": "number",  # Cambiar de float a number
                        "format": "float",  # Indicar que es un número con decimales
                        "description": "Cost price. Must be not null and a positive number."
                    },
                    "sale_price": {
                        "type": "number",  # Cambiar de float a number
                        "format": "float",  # Indicar que es un número con decimales
                        "description": "Sale price. Must be not null and a positive number."
                    }
                },
                "required": ["cost_price", "sale_price"]
            }
        }
    ],
    "responses": {
        201: {
            "description": "Price created successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "description": "Price id"
                    },
                    "cost_price": {
                        "type": "number",  # Cambiar de float a number
                        "format": "float",  # Indicar que es un número con decimales
                        "description": "Cost price."
                    },
                    "sale_price": {
                        "type": "number",  # Cambiar de float a number
                        "format": "float",  # Indicar que es un número con decimales
                        "description": "Sale price."
                    }
                }
            },
        400: {
            "description": "Invalid input",
            "schema": {
                "type": "object",
                "properties": {
                    "error": {
                        "type": "string",
                        "description": "Error message"
                    }
                }
            },
        },
        500: {
            "description": "Internal error",
            "schema": {
                "type": "object",
                "properties": {
                    "error": {
                        "type": "string",
                        "description": "Error message"
                    },
                    "except": {
                        "type": "string",
                        "description": "Exception message"
                    }
                }
            },
        }
    }
}
}