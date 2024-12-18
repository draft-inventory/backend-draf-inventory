from flasgger import swag_from

# Create_category_swagger
create_category_swagger = {
    "tags": ["Category"],
    "summary": "Create a new category",
    "description": "Create a new category",
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
                        "description": "Category name. Must be 2-15 characters, no numbers, and only valid Latin characters."
                    }
                },
                "required": ["name"]
            }
        }
    ],
    "responses": {
        201: {
            "description": "Category created successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "description": "Category id"
                    },
                    "name": {
                        "type": "string",
                        "description": "Category name"
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
                        },
                        "except": {
                            "type": "string",
                            "description": "Exception message"
                        }
                    }
                }
            }
        }
    }
}
