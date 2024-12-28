from flasgger import swag_from

# Create_price_swagger
create_price_swagger = {
    "tags": ["Price"],
    "summary": "Create a new price",
    "description": "Create a new price",
    "requestBody": {
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "cost_price": {
                            "type": "number",
                            "format": "float",
                            "description": "Cost price. Must be a positive number."
                        },
                        "sale_price": {
                            "type": "number",
                            "format": "float",
                            "description": "Sale price. Must be a positive number."
                        }
                    }
                }
            }
        }
    },
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
                        "type": "number",
                        "format": "float",
                        "description": "Cost price."
                    },
                    "sale_price": {
                        "type": "number",
                        "format": "float",
                        "description": "Sale price."
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

get_all_prices_swagger = {
    "tags": ["Price"],
    "summary": "Get all prices",
    "description": "Get all prices",
    "responses": {
        200: {
            "description": "Prices found",
            "schema": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer",
                            "description": "Price id"
                        },
                        "cost_price": {
                            "type": "number",
                            "format": "float",
                            "description": "Cost price."
                        },
                        "sale_price": {
                            "type": "number",
                            "format": "float",
                            "description": "Sale price."
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

get_price_by_id_swagger = {
    "tags": ["Price"],
    "summary": "Get price by ID",
    "description": "Get price by ID",
    "parameters": [
        {
            "name": "price_id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "Price ID"
        }
    ],
    "responses": {
        200: {
            "description": "Price found",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "description": "Price id"
                    },
                    "cost_price": {
                        "type": "number",
                        "format": "float",
                        "description": "Cost price."
                    },
                    "sale_price": {
                        "type": "number",
                        "format": "float",
                        "description": "Sale price."
                    }
                }
            }
        },
        404: {
            "description": "Price not found",
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

update_price_swagger = {
    "tags": ["Price"],
    "summary": "Update price",
    "description": "Update price",
    "requestBody": {
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "cost_price": {
                            "type": "number",
                            "format": "float",
                            "description": "Cost price. Must be a positive number."
                        },
                        "sale_price": {
                            "type": "number",
                            "format": "float",
                            "description": "Sale price. Must be a positive number."
                        }
                    }
                }
            }
        }
    },
    "parameters": [
        {
            "name": "price_id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "Price ID"
        }
    ],
    "responses": {
        200: {
            "description": "Price updated successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "description": "Price id"
                    },
                    "cost_price": {
                        "type": "number",
                        "format": "float",
                        "description": "Cost price."
                    },
                    "sale_price": {
                        "type": "number",
                        "format": "float",
                        "description": "Sale price."
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

patch_price_swagger = {
    "tags": ["Price"],
    "summary": "Patch price",
    "description": "Patch price",
    "requestBody": {
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "cost_price": {
                            "type": "number",
                            "format": "float",
                            "description": "Cost price. Must be a positive number."
                        },
                        "sale_price": {
                            "type": "number",
                            "format": "float",
                            "description": "Sale price. Must be a positive number."
                        }
                    }
                }
            }
        }
    },
    "parameters": [
        {
            "name": "price_id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "Price ID"
        }
    ],
    "responses": {
        200: {
            "description": "Price patched successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "description": "Price id"
                    },
                    "cost_price": {
                        "type": "number",
                        "format": "float",
                        "description": "Cost price."
                    },
                    "sale_price": {
                        "type": "number",
                        "format": "float",
                        "description": "Sale price."
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

delete_price_swagger = {
    "tags": ["Price"],
    "summary": "Delete price",
    "description": "Delete price",
    "parameters": [
        {
            "name": "price_id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "Price ID"
        }
    ],
    "responses": {
        200: {
            "description": "Price deleted successfully",
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
            "description": "Price not found",
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
