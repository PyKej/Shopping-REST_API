from models.product import Product, ProductCreate

# In-memory "database"
_products: list[Product] = []
_next_id: int = 0

def add_product(product_data: ProductCreate) -> Product:
    global _next_id
    
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

def delete_product(product_id: int) -> bool:
    global _products
    before = len(_products)
    _products = [p for p in _products if p.id != product_id]
    return len(_products) < before
