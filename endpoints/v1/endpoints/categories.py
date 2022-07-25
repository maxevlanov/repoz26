from fastapi import APIRouter, HTTPException, Query, Depends

from schemas import CategorySchema, CategoryInDBShema
from crud_async import CRUDCategory


category_router = APIRouter(
    prefix="/category"
)


async def check_category_id(category_id: int) -> int:
    if category_id < 1:
        raise HTTPException(status_code=404, detail="argument category_id must be equal 1")
    category = await CRUDCategory.get(category_id=category_id)
    if category:
        return category_id
    else:
        raise HTTPException(status_code=404, detail="invalid category_id argument")


@category_router.get("/get", response_model=CategoryInDBShema, tags=["Category"])
async def get_category(category_id: int = Depends(check_category_id)):
   return await CRUDCategory.get(category_id=category_id)


@category_router.get("/all", response_model=list[CategoryInDBShema], tags=["Category"])
async def get_all_categories(parent_id: int = Query(ge=1)):
    categories = await CRUDCategory.get_all(parent_id=parent_id)
    return categories


@category_router.post("/add", responcse_model=CategoryInDBShema, tags=["Category"])
async def add_category(category: CategorySchema):
    category = await CRUDCategory.add(category=category)
    if category:
        return category
    else:
        raise HTTPException(status_code=404, detail="category is exist")


@category_router.delete("/del", tags=["Category"])
async def delete_category(category_id: int = Depends(check_category_id):
    await CRUDCategory.delete(category_id=category_id)
    raise HTTPException(status_code=200, detail="category was deleted")


@category_router.put("/update", tags=["Category"])
async def update_category(category: CategoryInDBShema):
    await CRUDCategory.update(category=category)
    raise HTTPException(status_code=200, detail="category was updated")