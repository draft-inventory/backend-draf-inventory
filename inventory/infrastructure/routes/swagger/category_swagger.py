from flasgger import swag_from

# Create_category_swagger
create_category_swagger = {
    "tags": ["Category"],
    "summary": "Create a new category",
    "description": "Create a new category in the system.",
    "requestBody": {
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Category name. Must be 2-15 characters, no numbers, and only valid Latin characters.",
                            "example": "Abarrotes"
                        }
                    },
                    "required": ["name"]
                }
            }
        }
    },
    "responses": {
        201: {
            "description": "Category created successfully.",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "integer",
                                "description": "Category ID.",
                                "example": 1
                            },
                            "name": {
                                "type": "string",
                                "description": "Category name.",
                                "example": "Abarrotes"
                            }
                        }
                    }
                }
            }
        },
        400: {
            "description": "Invalid input. Validation failed.",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "error": {
                                "type": "string",
                                "description": "Error message.",
                                "example": "Invalid name. Name must be 2-15 characters, no numbers, and only valid Latin characters."
                            }
                        }
                    }
                }
            }
        },
        500: {
            "description": "Internal server error.",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "error": {
                                "type": "string",
                                "description": "Error message.",
                                "example": "Internal error"
                            },
                            "except": {
                                "type": "string",
                                "description": "Exception message.",
                                "example": "Detailed exception information"
                            }
                        }
                    }
                }
            }
        }
    }
}


# Get_category_by_id_swagger
get_category_by_id_swagger = {
    "tags": ["Category"],
    "summary": "Get category by ID",
    "description": "Retrieve a category by its ID.",
    "parameters": [
        {
            "name": "category_id",
            "in": "path",
            "required": True,
            "description": "ID of the category to retrieve.",
            "schema": {
                "type": "integer",
                "example": 1
            }
        }
    ],
    "responses": {
        200: {
            "description": "Category retrieved successfully.",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "integer",
                                "description": "Category ID.",
                                "example": 1
                            },
                            "name": {
                                "type": "string",
                                "description": "Category name.",
                                "example": "Abarrotes"
                            }
                        }
                    }
                }
            }
        },
        404: {
            "description": "Category not found.",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "error": {
                                "type": "string",
                                "description": "Error message.",
                                "example": "Category not found."
                            }
                        }
                    }
                }
            }
        }
    }
}

# Get_all_categories_swagger
get_all_categories_swagger = {
    "tags": ["Category"],
    "summary": "Get all categories",
    "description": "Retrieve all categories.",
    "responses": {
        200: {
            "description": "List of all categories.",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer",
                                    "description": "Category ID.",
                                    "example": 1
                                },
                                "name": {
                                    "type": "string",
                                    "description": "Category name.",
                                    "example": "Abarrotes"
                                }
                            }
                        }
                    }
                }
            }
        },
        500: {
            "description": "Internal error.",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "error": {
                                "type": "string",
                                "description": "Error message.",
                                "example": "Internal server error."
                            }
                        }
                    }
                }
            }
        }
    }
}

# Update_category_swagger
update_category_swagger = {
    "tags": ["Category"],
    "summary": "Update a category",
    "description": "Update an existing category by its ID.",
    "parameters": [
        {
            "name": "category_id",
            "in": "path",
            "required": True,
            "description": "ID of the category to update.",
            "schema": {
                "type": "integer",
                "example": 1
            }
        }
    ],
    "requestBody": {
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "New name of the category.",
                            "example": "Electronics"
                        }
                    },
                    "required": ["name"]
                }
            }
        }
    },
    "responses": {
        200: {
            "description": "Category updated successfully.",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "integer",
                                "description": "Category ID.",
                                "example": 1
                            },
                            "name": {
                                "type": "string",
                                "description": "Updated category name.",
                                "example": "Electronics"
                            }
                        }
                    }
                }
            }
        },
        404: {
            "description": "Category not found.",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "error": {
                                "type": "string",
                                "description": "Error message.",
                                "example": "Category not found."
                            }
                        }
                    }
                }
            }
        }
    }
}

# Delete_category_swagger
delete_category_swagger = {
    "tags": ["Category"],
    "summary": "Delete a category",
    "description": "Delete a category by its ID.",
    "parameters": [
        {
            "name": "category_id",
            "in": "path",
            "required": True,
            "description": "ID of the category to delete.",
            "schema": {
                "type": "integer",
                "example": 1
            }
        }
    ],
    "responses": {
        200: {
            "description": "Category deleted successfully.",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "message": {
                                "type": "string",
                                "description": "Success message.",
                                "example": "Category deleted successfully."
                            }
                        }
                    }
                }
            }
        },
        404: {
            "description": "Category not found.",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "error": {
                                "type": "string",
                                "description": "Error message.",
                                "example": "Category not found."
                            }
                        }
                    }
                }
            }
        }
    }
}
