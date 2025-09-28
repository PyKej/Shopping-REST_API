from models.product import Product, ProductCreate, ProductUpdate

# In-memory "database"
_products: list[Product] = []
_next_id: int = 0

def add_product(product_data: ProductCreate) -> Product:
    global _next_id

#     product = Product(
#     id=_next_id,
#     name=product_data.name,
#     description=product_data.description,
#     amount=product_data.amount,
#     unit=product_data.unit,
#     price=product_data.price
#   )
    product = Product(id=_next_id, **product_data.model_dump()) # Sexy line which creates a Product from ProductCreate
    _next_id += 1
    _products.append(product)
    return product

def get_all_products() -> list[Product]:
    return _products

def get_product(product_id: int) -> Product | None:
    for p in _products:
        if p.id == product_id:
            return p
    return None



def update_product(product_id: int, product_data: ProductUpdate) -> Product | None:
    p = get_product(product_id)
    if p:
        if product_data.name:
            p.name = product_data.name
        if product_data.description:
            p.description = product_data.description
        if product_data.amount:
            p.amount = product_data.amount
        if product_data.unit:
            p.unit = product_data.unit
        if product_data.price:
            p.price = product_data.price
        return p
    # Not implemented
    return None

def increase_product_amount(product_id: int, amount: int) -> Product | None:
    p = get_product(product_id)
    if p:
        p.amount += amount
        return p.amount
    return None

def decrese_product_amount(product_id: int, amount: int) -> Product | None:
    p = get_product(product_id)
    if p:
        p.amount -= amount
        return p.amount
    return None

def delete_product(product_id: int) -> bool:
    global _products
    for i, p in enumerate(_products):
        if p.id == product_id:
            del _products[i]
            return True
    return False

