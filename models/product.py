from pydantic import BaseModel
from typing import Optional



# Input model for creating a new Product
class ProductCreate(BaseModel):
    name: str
    description: str
    amount: int
    unit: str
    price: float

# Oudput model for Product
class Product(ProductCreate):
    id: Optional[int] = None  # system will fill this in
    name: str
    description: str
    amount: int
    unit: str
    price: float


    # # Constructor I don' need if I use dataclass
    # def __init__(self, id:int, name:str, description:str, amount:int, unit:str, price:float) -> None:
    #     self.id = id
    #     self.name = name
    #     self.description = description
    #     self.amount = amount
    #     self.unit = unit
    #     self.price = price
   

