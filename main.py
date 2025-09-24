from fastapi import FastAPI, HTTPException
from models.product import Product, ProductCreate
from models.cart import Cart
import repositories.product_repo as product_repo


# create the app
app = FastAPI()

def fill_data()->None:
    product_repo.add_product(ProductCreate(name="Apple", description="A juicy red apple", amount=10, unit="pieces", price=0.5))
    product_repo.add_product(ProductCreate(name="Banana", description="A ripe banana", amount=20, unit="pieces", price=0.3))
    product_repo.add_product(ProductCreate(name="Orange", description="A sweet orange", amount=15, unit="pieces", price=0.4))
    product_repo.add_product(ProductCreate(name="Milk", description="A bottle of milk", amount=5, unit="liters", price=1.2))
    product_repo.add_product(ProductCreate(name="Bread", description="A loaf of bread", amount=8, unit="pieces", price=1.5))
    product_repo.add_product(ProductCreate(name="Eggs", description="A dozen eggs", amount=12, unit="pieces", price=2.0))


fill_data()

@app.get("/product/")
async def get_products():
    return product_repo.get_all_products()

@app.get("/product/{product_id}")
async def read_item(product_id: int):
    p = product_repo.get_product(product_id)
    if p is None:
       raise HTTPException(status_code=404, detail="Product not found")
    return {
        "id": p.id, 
        "name": p.name, 
        "description": p.description, 
        "amount": p.amount, 
        "unit": p.unit, 
        "price": p.price
    }

@app.post("/product/", response_model=Product)
async def create_product(product: ProductCreate):
    return product_repo.add_product(product)



