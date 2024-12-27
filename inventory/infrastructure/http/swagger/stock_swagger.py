from flasgger import swag_from

create_stock_swagger = {
    "tags": ["Stock"],
    "summary": "Create a new stock",
    "description": "Create a new stock entry in the inventory.",
    "requestBody": {
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "movement_type": {
                            "type": "string",
                            "description": "Type of movement (e.g., ENTRADA, SALIDA).",
                            "example": "IN"
                        },
                        "quantity_id": {
                            "type": "integer",
                            "description": "ID of the associated quantity.",
                            "example": 1
                        }
                    },
                    "required": ["movement_type", "quantity_id"]
                }
            }
        }
    },
    "responses": {
        201: {
            "description": "Stock created successfully",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "integer",
                                "description": "ID of the created stock entry."
                            },
                            "movement_type": {
                                "type": "string",
                                "description": "Type of movement."
                            },
                            "quantity_id": {
                                "type": "integer",
                                "description": "ID of the associated quantity."
                            }
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
                            "error": {
                                "type": "string",
                                "description": "Error message."
                            }
                        }
                    }
                }
            }
        },
        500: {
            "description": "Internal server error",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "error": {
                                "type": "string",
                                "description": "Error message."
                            }
                        }
                    }
                }
            }
        }
    }
}

get_stock_by_id_swagger = {
    "tags": ["Stock"],
    "summary": "Retrieve a stock entry by ID",
    "description": "Fetch details of a stock entry using its ID.",
    "parameters": [
        {
            "name": "stock_id",
            "in": "path",
            "required": True,
            "schema": {
                "type": "integer"
            },
            "description": "ID of the stock entry."
        }
    ],
    "responses": {
        200: {
            "description": "Stock details retrieved successfully",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "integer",
                                "description": "ID of the stock entry."
                            },
                            "movement_type": {
                                "type": "string",
                                "description": "Type of movement."
                            },
                            "quantity_id": {
                                "type": "integer",
                                "description": "ID of the associated quantity."
                            }
                        }
                    }
                }
            }
        },
        404: {
            "description": "Stock entry not found",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "error": {
                                "type": "string",
                                "description": "Error message."
                            }
                        }
                    }
                }
            }
        },
        500: {
            "description": "Internal server error",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "error": {
                                "type": "string",
                                "description": "Error message."
                            }
                        }
                    }
                }
            }
        }
    }
}

update_movement_type_swagger = {
    "tags": ["Stock"],
    "summary": "Update the movement type of a stock entry",
    "description": "Update the movement type for a specific stock entry.",
    "parameters": [
        {
            "name": "stock_id",
            "in": "path",
            "required": True,
            "schema": {
                "type": "integer"
            },
            "description": "ID of the stock entry."
        }
    ],
    "requestBody": {
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "movement_type": {
                            "type": "string",
                            "description": "New movement type. Must be one of the valid types.",
                            "example": "OUT"
                        }
                    },
                    "required": ["movement_type"]
                }
            }
        }
    },
    "responses": {
        200: {
            "description": "Movement type updated successfully",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "integer",
                                "description": "ID of the stock entry."
                            },
                            "movement_type": {
                                "type": "string",
                                "description": "Updated movement type."
                            }
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
                            "error": {
                                "type": "string",
                                "description": "Error message."
                            }
                        }
                    }
                }
            }
        },
        404: {
            "description": "Stock entry not found",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "error": {
                                "type": "string",
                                "description": "Error message."
                            }
                        }
                    }
                }
            }
        },
        500: {
            "description": "Internal server error",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "error": {
                                "type": "string",
                                "description": "Error message."
                            }
                        }
                    }
                }
            }
        }
    }
}

delete_stock_swagger = {
    "tags": ["Stock"],
    "summary": "Delete a stock entry",
    "description": "Remove a stock entry from the inventory.",
    "parameters": [
        {
            "name": "stock_id",
            "in": "path",
            "required": True,
            "schema": {
                "type": "integer"
            },
            "description": "ID of the stock entry."
        }
    ],
    "responses": {
        200: {
            "description": "Stock entry deleted successfully",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "message": {
                                "type": "string",
                                "description": "Success message."
                            }
                        }
                    }
                }
            }
        },
        404: {
            "description": "Stock entry not found",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "error": {
                                "type": "string",
                                "description": "Error message."
                            }
                        }
                    }
                }
            }
        },
        500: {
            "description": "Internal server error",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "error": {
                                "type": "string",
                                "description": "Error message."
                            }
                        }
                    }
                }
            }
        }
    }
}
