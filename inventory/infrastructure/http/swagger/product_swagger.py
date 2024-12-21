from flasgger import swag_from

# Create Product Swagger
create_product_swagger = {
    'tags': ['Product'],
    'summary': 'Create Product',
    'description': 'Create a new product with validations and auto-generated product code',
    "requestBody": {
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "example": "Product Name",
                            "description": "Name of the product. Only alphabetic characters and spaces are allowed."
                        },
                        "description": {
                            "type": "string",
                            "example": "Product Description",
                            "description": "Description of the product. Alphanumeric characters and spaces are allowed."
                        },
                        "expiration_date": {
                            "type": "string",
                            "format": "date",
                            "example": "2024-12-31",
                            "description": "Expiration date of the product in YYYY-MM-DD format."
                        },
                        "location_id": {
                            "type": "integer",
                            "example": 1,
                            "description": "Optional location identifier for the product."
                        },
                        "category_id": {
                            "type": "integer",
                            "example": 1,
                            "description": "ID of the category. Must reference an existing category."
                        },
                        "quantity_id": {
                            "type": "integer",
                            "example": 2,
                            "description": "ID of the quantity. Must reference an existing quantity."
                        }
                    },
                    "required": ["name", "description", "category_id", "quantity_id"]
                }
            }
        }
    },
    'responses': {
        '201': {
            'description': 'Product created successfully',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'id': {
                                'type': 'integer',
                                'example': 1,
                                'description': "Product ID."
                            },
                            'name': {
                                'type': 'string',
                                'example': 'Product Name',
                                'description': "Name of the product."
                            },
                            'description': {
                                'type': 'string',
                                'example': 'Product Description',
                                'description': "Description of the product."
                            },
                            'product_code': {
                                'type': 'string',
                                'example': 'PN_E1',
                                'description': "Auto-generated product code based on the name."
                            },
                            'expiration_date': {
                                'type': 'string',
                                'example': '2024-12-31',
                                'description': "Expiration date of the product."
                            },
                            'location_id': {
                                'type': 'integer',
                                'example': 1,
                                'description': "Location ID of the product."
                            },
                            'category_id': {
                                'type': 'integer',
                                'example': 1,
                                'description': "Category ID of the product."
                            },
                            'quantity_id': {
                                'type': 'integer',
                                'example': 2,
                                'description': "Quantity ID of the product."
                            }
                        }
                    }
                }
            }
        },
        '400': {
            'description': 'Invalid input',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'error': {
                                'type': 'string',
                                'example': 'Name must only contain alphabetic characters and spaces.'
                            }
                        }
                    }
                }
            }
        },
        '500': {
            'description': 'Internal error',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'error': {
                                'type': 'string',
                                'example': 'Internal error occurred while creating the product.'
                            }
                        }
                    }
                }
            }
        }
    }
}
