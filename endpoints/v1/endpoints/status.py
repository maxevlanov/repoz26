from fastapi import APIRouter, HTTPException, Query

from schemas import StatusSchema, StatusInDBShema
from crud_async import CRUDStatus


status_router = APIRouter(
    prefix="/status"
)


@status_router.get("/get", response_model=StatusInDBShema, tags=["Status"])
async def get_status(status_id: int = Query(ge=1)):
    status = await CRUDStatus.get(status_id=status_id)
    if status:
        return status
    else:
        raise HTTPException(status_code=404, detail=f"status with id {status_id} not found")

@status_router.get("/all", response_model=list[StatusInDBShema], tags=["Status"])
async def get_all_statuses(status_id: int = Query(ge=1)):
    statuses = await CRUDStatus.get_all(status_id=status_id)
    return statuses


@status_router.post("/add", response_model=StatusInDBShema, tags=["Status"])
async def add_status(status: StatusSchema):
    status = await CRUDStatus.add(status=status)
    if status:
        return status
    else:
        raise HTTPException(status_code=404, detail="status is exist")


@status_router.delete("/del", tags=["Status"])
async def delete_status(status_id: int):
    await CRUDStatus.delete(status_id=status_id)
    raise HTTPException(status_code=200, detail="status was deleted")


@status_router.put("/update", tags=["Status"])
async def update_status(status: StatusInDBShema):
    await CRUDStatus.update(status=status)
    raise HTTPException(status_code=200, detail="status was updated")