from flasgger import swag_from

# Create_quantity_history_swagger
create_quantity_history_swagger = {
    "tags": ["Quantity History"],
    "summary": "Create a new quantity history",
    "description": "Create a new quantity history",
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "quantity_id": {
                        "type": "integer",
                        "description": "Quantity id. Must be a positive number."
                    },
                    "date": {
                        "type": "string",
                        "description": "Date. Must be a valid date."
                    },
                    "sold_quantity": {
                        "type": "integer",
                        "description": "Sold quantity. Must be a positive number."
                    }
                },
                "required": ["quantity_id", "date", "sold_quantity"]
            }
        }
    ],
    "responses": {
        201: {
            "description": "Quantity history created successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "description": "Quantity history id"
                    },
                    "quantity_id": {
                        "type": "integer",
                        "description": "Quantity id"
                    },
                    "date": {
                        "type": "string",
                        "description": "Date"
                    },
                    "sold_quantity": {
                        "type": "integer",
                        "description": "Sold quantity"
                    },
                    "remaining_quantity": {
                        "type": "integer",
                        "description": "Remaining quantity after the sale"
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
        }
    }
}
