from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(
    title='API quản lý sản phẩm cơ bản',
    description='API quản lý sản phẩm cơ bản',
    version='1.0.0'
)

products = [
    {"id": 1, "name": "Keyboard", "price": 500000},
    {"id": 2, "name": "Mouse", "price": 300000}
]

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=0)
    price: int = Field(..., gt=0)
    
@app.post("/products", status_code=201)
def product_create(product: ProductCreate):
    new_product = {
        "id": len(products) + 1,
        "name": product.name,
        "price": product.price
    }
    
    products.append(new_product)
    
    return {
        "message": "Thêm sản phẩm thành công",
        "data": new_product
    }

@app.get("/products")
def get_product():
    return {
        "message": "Lấy danh sách sản phẩm thành công",
        "data": products
    }    
    
@app.delete("/products/{product_id}")
def product_delete_by_id(product_id: int):
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            return {
                "message": "Xóa sản phẩm thành công"
            }
            
    raise HTTPException(
        status_code=404,
        detail="Không tìm thấy sản phẩm cần xóa"
    )