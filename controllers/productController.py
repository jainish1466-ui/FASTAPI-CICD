from fastapi import Response
from pydantic import BaseModel
from typing import Optional
from models.productModel import Product
from dbConnect import productCollection 

# List to store products
products = []
product_id = 0

async def create_product_controller(product: Product, response: Response):
    try:
        result = await productCollection.insert_one(product.dict())
        # product_id += 1
        product.id = str(result.inserted_id)
        # products.append(product)

        response.status_code = 201
        return {
            "isSuccess": True,
            "message": "Product created successfully",
            "data": product
        }
    except Exception as e:
        print(e)
        response.status_code = 500
        return {
            "isSuccess": False,
            "message": str(e)
        }

async def get_products_controller(response: Response):
    try:
        productss = []
        async for product in productCollection.find():
            productss.append(Product(**product))

        return {"products": productss, "issuccess" : True}
    except Exception as e:
        print (e)
        response.status_code = 500
        return {"message": "Error fetching products", "issuccess" : False}

def get_product_by_id(id: int, response: Response):
    for product in products:
        if product.id == id:
            response.status_code = 200
            return {
                "isSuccess": True,
                "data": product
            }
        
            response.status_code = 404
            return {
                "isSuccess": False,
                "message": "Product not found"
            }



def update_product_controller(id: int, product: Product, response: Response):
    for i in range(len(products)):
        if products[i].id == id:
            product.id = id
            products[i] = product

            response.status_code = 200
            return {
                "isSuccess": True,
                "message": "Product updated successfully",
                "data": product
            }

    response.status_code = 404
    return {
        "isSuccess": False,
        "message": "Product not found"
    }

def delete_product_controller(id: int, response: Response):
    for i in range(len(products)):
        if products[i].id == id:
            products.pop(i)

            response.status_code = 200
            return {
                "isSuccess": True,
                "message": "Product deleted successfully"
            }

    response.status_code = 404
    return {
        "isSuccess": False,
        "message": "Product not found"
    }