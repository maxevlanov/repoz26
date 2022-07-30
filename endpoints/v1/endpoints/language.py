from fastapi import APIRouter, HTTPException, Query

from schemas import LanguageSchema, LanguageInDBShema
from crud_async import CRUDLanguage


language_router = APIRouter(
    prefix="/language"
)


@language_router.get("/get", response_model=LanguageInDBShema, tags=["Language"])
async def get_language(language_id: int = Query(ge=1)):
    language = await CRUDLanguage.get(language_id=language_id)
    if language:
        return language
    else:
        raise HTTPException(status_code=404, detail=f"language with id {language_id} not found")

@language_router.get("/all", response_model=list[LanguageInDBShema], tags=["Language"])
async def get_all_languages(language_code: int = Query(ge=1)):
    languages = await CRUDLanguage.get_all(language_code=language_code)
    return languages


@language_router.post("/add", response_model=LanguageInDBShema, tags=["Language"])
async def add_language(language: LanguageSchema):
    language = await CRUDLanguage.add(language=language)
    if language:
        return language
    else:
        raise HTTPException(status_code=404, detail="language is exist")


@language_router.delete("/del", tags=["Language"])
async def delete_language(language_id: int):
    await CRUDLanguage.delete(language_id=language_id)
    raise HTTPException(status_code=200, detail="language was deleted")


@language_router.put("/update", tags=["Language"])
async def update_language(language: LanguageInDBShema):
    await CRUDLanguage.update(language=language)
    raise HTTPException(status_code=200, detail="language was updated")