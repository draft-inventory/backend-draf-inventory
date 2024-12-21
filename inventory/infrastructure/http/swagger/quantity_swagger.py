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

get_all_quantities_swagger = {
    "tags": ["Quantity"],
    "summary": "Get all quantities",
    "description": "Get all quantities",
    "parameters": [],
    "responses": {
        200: {
            "description": "Quantities retrieved successfully",
            "schema": {
                "type": "array",
                "items": {
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

get_quantity_by_id_swagger = {
    "tags": ["Quantity"],
    "summary": "Get quantity by id",
    "description": "Get quantity by id",
    "parameters": [
        {
            "name": "quantity_id",
            "in": "path",
            "required": True,
            "type": "integer",
            "description": "Quantity id"
        }
    ],
    "responses": {
        200: {
            "description": "Quantity retrieved successfully",
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
        404: {
            "description": "Quantity not found",
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

update_quantity_swagger = {
    "tags": ["Quantity"],
    "summary": "Update quantity",
    "description": "Update quantity",
    "parameters": [
        {
            "name": "quantity_id",
            "in": "path",
            "required": True,
            "type": "integer",
            "description": "Quantity id"
        },
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
        200: {
            "description": "Quantity updated successfully",
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

delete_quantity_swagger = {
    "tags": ["Quantity"],
    "summary": "Delete quantity",
    "description": "Delete quantity",
    "parameters": [
        {
            "name": "quantity_id",
            "in": "path",
            "required": True,
            "type": "integer",
            "description": "Quantity id"
        }
    ],
    "responses": {
        200: {
            "description": "Quantity deleted successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "Message"
                    }
                }
            }
        },
        404: {
            "description": "Quantity not found",
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
