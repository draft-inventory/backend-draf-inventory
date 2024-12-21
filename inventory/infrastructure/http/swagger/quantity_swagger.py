from flasgger import swag_from

# Create_quantity_swagger
create_quantity_swagger = {
    "tags": ["Quantity"],
    "summary": "Create a new quantity",
    "description": "Create a new quantity",
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "initial_quantity": {
                        "type": "integer",
                        "description": "Initial quantity. Must be a positive number."
                    },
                    "progress_quantity": {
                        "type": "integer",
                        "description": "Progress quantity. Must be a positive number."
                    }
                },
                "required": ["initial_quantity", "progress_quantity"]
            }
        }
    ],
    "responses": {
        201: {
            "description": "Quantity created successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "description": "Quantity id"
                    },
                    "initial_quantity": {
                        "type": "integer",
                        "description": "Initial quantity"
                    },
                    "progress_quantity": {
                        "type": "integer",
                        "description": "Progress quantity"
                    }
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
            }
        },
        500: {
            "description": "Internal error",
            "schema": {
                "type": "object",
                "properties": {
                    "error": {
                        "type": "string",
                        "description": "Error message"
                    }
                }
            }
        }
    }
}