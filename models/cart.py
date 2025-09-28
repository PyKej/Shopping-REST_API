from pydantic import BaseModel
from typing import Optional
from models.product import Product


class CartItem(BaseModel):
    product_id: int
    amount: int
class Cart(BaseModel):
    id: int
    shopping_list: list[CartItem]
    payed: bool




