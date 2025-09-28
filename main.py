from fastapi import FastAPI, HTTPException
from models.product import Product, ProductCreate, ProductUpdate, ProductUpdateAmmount
from models.cart import Cart
import repositories.product_repo as product_repo

import repositories.cart_repo as cart_repo


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

@app.get("/product/{product_id}/amount")
async def get_product_amout(product_id:int):
    p = product_repo.get_product(product_id)
    return {
        "amount": p.amount
    }

@app.post("/product/{product_id}/amount")
async def update_product_amount(product_id:int, amount:ProductUpdateAmmount):
    amount = product_repo.increase_product_amount(product_id, amount.amount)
    if amount is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"amount": amount}

@app.post("/product/", response_model=Product)
async def create_product(product: ProductCreate):
    return product_repo.add_product(product)

@app.put("/product/{product_id}", response_model=Product)
async def update_product(product_id: int, product: ProductUpdate):
    p = product_repo.update_product(product_id, product)
    if p is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return p

@app.delete("/product/{product_id}")
async def delete_product(product_id: int):
    success = product_repo.delete_product(product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"detail": "Product deleted"}

@app.post("/cart/")
async def cart_create() -> Cart:
    return cart_repo.cart_create()

@app.get("/cart/all")
async def cart_create() -> list[Cart]:
    return cart_repo.get_all_carts()

@app.get("/cart/{cart_id}")
async def get_cart(cart_id : int) -> Cart|None:
    c = cart_repo.get_cart(cart_id)
    if c is None:
        raise HTTPException(status_code=404, detail="Cart not found")
    return c


@app.post("/cart/{cart_id}/{product_id}/{amount_to_transfer}/add")
async def add_cart(cart_id : int, product_id:int, amount_to_transfer:int) -> Cart|None:
    return cart_repo.add_cart(cart_id, product_id, amount_to_transfer)

@app.put("/cart/{cart_id}/pay")
async def pay_for_cart(cart_id : int) -> Cart|None:
    c = cart_repo.get_cart(cart_id)
    if c is None:
        raise HTTPException(status_code=404, detail="Cart not found")
    else:
        cart_repo.pay_for_cart(c)
    return c
