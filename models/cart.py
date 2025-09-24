from dataclasses import dataclass
from models.product import Product

@dataclass
class Cart:
    id: int
    shopping_list: list[Product]
    payed: bool