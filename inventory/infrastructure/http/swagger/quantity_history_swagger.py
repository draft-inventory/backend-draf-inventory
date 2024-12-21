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


get_all_quantity_histories_swagger = {
    "tags": ["Quantity History"],
    "summary": "Get all quantity histories",
    "description": "Get all quantity histories",
    "parameters": [],
    "responses": {
        200: {
            "description": "Quantity histories retrieved successfully",
            "schema": {
                "type": "array",
                "items": {
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
            }
        }
    }
}

get_quantity_history_by_id_swagger = {
    "tags": ["Quantity History"],
    "summary": "Get quantity history by id",
    "description": "Get quantity history by id",
    "parameters": [
        {
            "name": "quantity_history_id",
            "in": "path",
            "required": True,
            "type": "integer",
            "description": "Quantity history id"
        }
    ],
    "responses": {
        200: {
            "description": "Quantity history retrieved successfully",
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
        404: {
            "description": "Quantity history not found",
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


get_quantity_by_quiantity_id_swagger = {
    "tags": ["Quantity History"],
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

delete_quantity_history_swagger = {
    "tags": ["Quantity History"],
    "summary": "Delete quantity history",
    "description": "Delete quantity history",
    "parameters": [
        {
            "name": "quantity_history_id",
            "in": "path",
            "required": True,
            "type": "integer",
            "description": "Quantity history id"
        }
    ],
    "responses": {
        200: {
            "description": "Quantity history deleted successfully",
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
            "description": "Quantity history not found",
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

update_quantity_history_swagger = {
    "tags": ["Quantity History"],
    "summary": "Update quantity history",
    "description": "Update quantity history",
    "requestBody": {
        "required": True,
        "content": {
            "application/json": {
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
        }
    },
    "parameters": [
        {
            "name": "quantity_history_id",
            "in": "path",
            "required": True,
            "schema": {
                "type": "integer",
                "example": 1
            },
            "description": "Quantity history id"
        }
    ],
    "responses": {
        200: {
            "description": "Quantity history updated successfully",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer", "description": "Quantity history id"},
                            "quantity_id": {"type": "integer", "description": "Quantity id"},
                            "date": {"type": "string", "description": "Date"},
                            "sold_quantity": {"type": "integer", "description": "Sold quantity"},
                            "remaining_quantity": {
                                "type": "integer",
                                "description": "Remaining quantity after the sale"
                            }
                        }
                    }
                }
            }
        },
        404: {
            "description": "Quantity history not found",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "error": {"type": "string", "description": "Error message"}
                        }
                    }
                }
            }
        },
        400: {
            "description": "Invalid input",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "error": {"type": "string", "description": "Error message"}
                        }
                    }
                }
            }
        },
        500: {
            "description": "Internal error",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "error": {"type": "string", "description": "Error message"}
                        }
                    }
                }
            }
        }
    }
}


patch_quantity_history_swagger = {
    "tags": ["Quantity History"],
    "summary": "Patch quantity history",
    "description": "Patch quantity history",
    "requestBody": {
        "required": True,
        "content": {
            "application/json": {
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
        }
    },
    "parameters": [
        {
            "name": "quantity_history_id",
            "in": "path",
            "required": True,
            "schema": {
                "type": "integer",
            },
            "description": "Quantity history id"
        }
    ],
    "responses": {
        200: {
            "description": "Quantity history patched successfully",
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
        404: {
            "description": "Quantity history not found",
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
