from fastapi import APIRouter, Response
from controllers.productController import create_product_controller,update_product_controller,get_products_controller,get_product_by_id,delete_product_controller
from models.productModel import Product

productRouter = APIRouter(
    prefix="/products",
    tags=["Products"]
)

# Create Product
@productRouter.post("/postproducts")
async def create_product(product: Product, response: Response):
    return await create_product_controller(product, response)

# Get All Products
@productRouter.get("/getproducts")
async def get_product( response: Response):
    return await get_products_controller(response)



# Get Product by ID
@productRouter.get("/getproducts/{id}")
def get_product(id: int, response: Response):
    return get_product_by_id(id, response)
    

# Update Product
@productRouter.put("/putproducts/{id}")
def update_product(id: int, product: Product, response: Response):
    return update_product_controller(id, product, response)


# Delete Product
@productRouter.delete("/deleteproducts/{id}")
def delete_product(id: int, response: Response):
    return delete_product_controller(id, response)