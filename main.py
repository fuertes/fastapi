from typing import List
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(
    title="Awazon",
    description="FastAPI example focusing on products",
    version="1.0.0"
)

class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int

products: List[Product] = [
    Product(id=1, name="RGB Mechanical Keyboard", price=59.99, stock=15),
    Product(id=2, name="Ergonomic Wireless Mouse", price=29.95, stock=30),
    Product(id=3, name="27'' 144Hz Gaming Monitor", price=219.00, stock=8),
]

@app.get("/products", response_model=List[Product], summary="Get all products")
def read_products():
    return products

@app.get("/products/{product_id}", response_model=Product, summary="Get product by ID")
def read_product_by_id(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
            
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product with ID {product_id} not found"
    )

@app.put("/products/{product_id}", response_model=Product, summary="Update a product")
def update_product(product_id: int, updated_product: Product):
    for index, product in enumerate(products):
        if product.id == product_id:
            products[index] = updated_product
            return updated_product

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Cannot update. Product with ID {product_id} not found"
    )