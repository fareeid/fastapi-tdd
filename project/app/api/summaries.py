# project/app/api/summaries.py


from fastapi import APIRouter, BackgroundTasks, HTTPException, Path

from app.api import crud  # type: ignore
from app.models.pydantic import (
    SummaryPayloadSchema,
    SummaryResponseSchema,
    SummaryUpdatePayloadSchema,
)
from app.models.tortoise import SummarySchema
from app.summarizer import generate_summary

router = APIRouter()


@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def create_summary(
    payload: SummaryPayloadSchema, background_tasks: BackgroundTasks
) -> SummaryResponseSchema:
    summary_id = await crud.post(payload)

    background_tasks.add_task(generate_summary, summary_id, payload.url)

    response_object = {"id": summary_id, "url": payload.url}
    return response_object  # type: ignore


# @router.post("/", response_model=SummaryResponseSchema, status_code=201)
# async def create_summary(payload: SummaryPayloadSchema) -> SummaryResponseSchema:
#     summary_id = await crud.post(payload)

#     response_object = {"id": summary_id, "url": payload.url}
#     return response_object  # type: ignore


@router.get("/{id}/", response_model=SummarySchema)
async def read_summary(id: int = Path(..., gt=0)) -> SummarySchema:  # type: ignore
    summary = await crud.get(id)
    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")
    return summary  # type: ignore


@router.get("/", response_model=list[SummarySchema])
async def read_all_summaries() -> list[SummarySchema]:
    return await crud.get_all()
    # return {"id": 3, "url": "qwert"}


@router.delete("/{id}/", response_model=SummaryResponseSchema)
async def delete_summary(id: int) -> SummaryResponseSchema:
    summary = await crud.get(id)
    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")

    await crud.delete(id)

    return summary  # type: ignore


@router.put("/{id}/", response_model=SummarySchema)
async def update_summary(id: int, payload: SummaryUpdatePayloadSchema) -> SummarySchema:
    summary = await crud.put(id, payload)
    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")

    return summary  # type: ignore
