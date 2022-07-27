from fastapi import FastAPI

from crud_async import CRUDCategory
from schemas import CategoryInDBSchema


app = FastAPI()


@app.get("/category", response_model=CategoryInDBSchema)
async def get_category(category_id: int):
    category = await CRUDCategory.get(category_id=category_id)
    if category:
        return
