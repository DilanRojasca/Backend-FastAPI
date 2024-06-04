from fastapi import APIRouter

router = APIRouter(prefix="/products")

products_list = ["apple", "banana", "orange", "product 4", "product 5"]

@router.get("/")
async def products():
    return products_list

@router.get("/{id}")
async def products(id: int):
    return products_list[id]