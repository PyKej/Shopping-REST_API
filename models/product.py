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
class Product(ProductCreate): # Inheritance from ProductCreate and adds id
    id: Optional[int] = None  
 
# ¨Input Model for updare of product
class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    amount: Optional[int] = None
    unit: Optional[str] = None
    price: Optional[float] = None

class ProductUpdateAmmount(BaseModel):
     amount: int

    # # Constructor I don' need if I use dataclass
    # def __init__(self, id:int, name:str, description:str, amount:int, unit:str, price:float) -> None:
    #     self.id = id
    #     self.name = name
    #     self.description = description
    #     self.amount = amount
    #     self.unit = unit
    #     self.price = price
   

