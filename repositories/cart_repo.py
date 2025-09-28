from models.cart import Cart, CartItem
from models.product import Product
import repositories.product_repo as product_repo

from fastapi import HTTPException

_carts : list[Cart] = []
_next_id: int = 0

def cart_create() -> Cart:
    global _next_id, _carts

    cart = Cart(id = _next_id, shopping_list = [], payed = False)
    _next_id += 1
    _carts.append(cart)
    return cart
    
def get_all_carts()-> list[Cart]:
    global _carts
    return _carts

def get_cart(cart_id : int) -> Cart|None:
    global _carts
    for c in _carts:
        if c.id ==cart_id:
            return c
    return None

def get_cart_item(cart: Cart, product_id : int) -> CartItem|None:
    for item in cart.shopping_list:
        if item.product_id == product_id:
            return item
    return None

def create_cart_item(cart: Cart, product_id: int, amount: int) -> CartItem:
    cart_item = CartItem(product_id = product_id, amount = amount)
    cart.shopping_list.append(cart_item)
    return None

def increse_cart_item(cart_item: CartItem, amount_to_transfer: int) -> None:
    cart_item.amount += amount_to_transfer

def transfer_from_product(product_item : Product, amount_to_transfer: int):
    if product_item:
        if product_item.amount > amount_to_transfer:
            product_repo.decrese_product_amount(product_item.id, amount_to_transfer)
        elif product_item.amount == amount_to_transfer:
            product_repo.delete_product(product_item.id)  
        else:
            raise HTTPException(status_code=400, detail="Not enought product in stock")
    else:
        raise HTTPException(status_code=404, detail="Product not found in Stock")


def transfer_to_cart(product_item : Product, cart: Cart, amount_to_transfer: int):
    if cart:
        item = get_cart_item(cart, product_item.id)
        if item:
            increse_cart_item(item, amount_to_transfer)
        else:
            create_cart_item(cart, product_item.id, amount_to_transfer)
    else:
        raise HTTPException(status_code=404, detail="Cart not found")

def add_cart(cart_id : int, product_id : int, amount_to_transfer: int) -> Cart|None:
    cart = get_cart(cart_id)
    product_item = product_repo.get_product(product_id)

    transfer_from_product(product_item, amount_to_transfer)
    transfer_to_cart(product_item, cart, amount_to_transfer)
    return cart
    
def pay_for_cart(cart :Cart)-> Cart:
    if cart.payed:
        raise HTTPException(status_code=400, detail="Cart was already payed")
    else:
        cart.payed = True