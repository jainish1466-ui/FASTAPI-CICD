from pydantic import BaseModel
from typing import Optional

# Product model
class Product(BaseModel):
    id: Optional[int] = None
    name: str
    price: int
    description: str
