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
                "type": "integer"
            }
        }
    ],
    "responses": {
        200: {
            "description": "Category retrieved successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "description": "Category ID"
                    },
                    "name": {
                        "type": "string",
                        "description": "Category name"
                    }
                }
            }
        },
        404: {
            "description": "Category not found",
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

get_all_categorys_swagger = {
    "tags": ["Category"],
    "summary": "Get all categories",
    "description": "Retrieve all categories.",
    "responses": {
        200: {
            "description": "List of all categories",
            "schema": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer",
                            "description": "Category ID"
                        },
                        "name": {
                            "type": "string",
                            "description": "Category name"
                        }
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
                "type": "integer"
            }
        },
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "New name of the category."
                    }
                },
                "required": ["name"]
            }
        }
    ],
    "responses": {
        200: {
            "description": "Category updated successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "description": "Category ID"
                    },
                    "name": {
                        "type": "string",
                        "description": "Updated category name"
                    }
                }
            }
        },
        404: {
            "description": "Category not found",
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
                "type": "integer"
            }
        }
    ],
    "responses": {
        200: {
            "description": "Category deleted successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "Success message"
                    }
                }
            }
        },
        404: {
            "description": "Category not found",
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
