from fastapi import APIRouter, HTTPException, Query

from schemas import ProductSchema, ProductInDBShema
from crud_async import CRUDProduct


product_router = APIRouter(
    prefix="/product"
)


@product_router.get("/get", response_model=ProductInDBShema, tags=["Product"])
async def get_product(product_id: int = Query(ge=1)):
    product = await CRUDProduct.get(product_id=product_id)
    if product:
        return product
    else:
        raise HTTPException(status_code=404, detail=f"product with id {product_id} not found")

@product_router.get("/all", response_model=list[ProductInDBShema], tags=["Product"])
async def get_all_products(category_id: int = Query(ge=1)):
    products = await CRUDProduct.get_all(category_id=category_id)
    return products


@product_router.post("/add", responcse_model=ProductInDBShema, tags=["Product"])
async def add_product(product: ProductSchema):
    product = await CRUDProduct.add(product=product)
    if product:
        return product
    else:
        raise HTTPException(status_code=404, detail="product is exist")


@product_router.delete("/del", tags=["Product"])
async def delete_product(product_id: int):
    await CRUDProduct.delete(product_id=product_id)
    raise HTTPException(status_code=200, detail="product was deleted")


@product_router.put("/update", tags=["Product"])
async def update_product(product: ProductInDBShema):
    await CRUDProduct.update(product=product)
    raise HTTPException(status_code=200, detail="product was updated")