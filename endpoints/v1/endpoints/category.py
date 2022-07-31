from datetime import datetime

from fastapi import APIRouter, HTTPException, Query, Depends, Request
from jose import JWTError, jwt

from schemas import CategorySchema, CategoryInDBSchema
from crud_async import CRUDCategory, CRUDUser
from core.config import CONFIG


category_router = APIRouter(
    prefix="/category"
)

async def validate_user(request: Request) -> bool:
   try:
       access_token = request.headers["Authorization"]
       if not access_token.startswith("Bearer "):
           return False
       access_token = access_token.replace("Bearer ", "")
       data = jwt.decode(access_token, CONFIG.AUTH.SECRET_KEY, algorithms=[CONFIG.AUTH.ALGORITHM])
       username = data["sub"]
       if not await CRUDUser.get_by_username(username=username):
           return False
       token_expire_date = data["exp"]
       token_expire_date = datetime.utcfromtimestamp(token_expire_date)
       if datetime.utcnow() < token_expire_date:
          return True
       else:
          return False
   except Exception:
       return False


async def check_category_id(category_id: int = Query(ge=1)) -> int:
    if category_id < 1:
        raise HTTPException(status_code=404, detail="argument category_id must be equal 1")
    category = await CRUDCategory.get(category_id=category_id)
    if category:
        return category_id
    else:
        raise HTTPException(status_code=404, detail="invalid category_id argument")


@category_router.get("/get", response_model=CategoryInDBSchema, tags=["Category"])
async def get_category(category_id: int = Depends(check_category_id)):
   return await CRUDCategory.get(category_id=category_id)


@category_router.get("/all", response_model=list[CategoryInDBSchema], tags=["Category"])
async def get_all_categories(parent_id: int = Query(ge=1)):
    categories = await CRUDCategory.get_all(parent_id=parent_id)
    return categories


@category_router.post("/add", responcse_model=CategoryInDBSchema, tags=["Category"])
async def add_category(category: CategorySchema, request: Request = Depends(validate_user)):
    if request:
        category = await CRUDCategory.add(category=category)
        if category:
            return category
        else:
            raise HTTPException(status_code=404, detail="category is exist")
    else:
        raise HTTPException(status_code=401, detail="Unautorized")


@category_router.delete("/del", tags=["Category"])
async def delete_category(category_id: int = Depends(check_category_id), request: Request = Depends(validate_user)):
    if request:
        await CRUDCategory.delete(category_id=category_id)
        raise HTTPException(status_code=200, detail="category was deleted")
    else:
        raise HTTPException(status_code=401, detail="Unautorized")

@category_router.put("/update", tags=["Category"])
async def update_category(category: CategoryInDBShema, request: Request = Depends(validate_user)):
    if request:
        await CRUDCategory.update(category=category)
        raise HTTPException(status_code=200, detail="category was updated")
    else:
        raise HTTPException(status_code=401, detail="Unautorized")