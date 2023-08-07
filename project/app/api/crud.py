# project/app/api/crud.py


from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary
from typing import Union


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(
        url=payload.url,
        summary="dummy summary",
    )
    await summary.save()
    print(summary.id)  # type: ignore
    return summary.id  # type: ignore


async def get(id: int) -> Union[dict, None]:
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary
    return None


async def get_all() -> list:
    summaries = await TextSummary.all().values()
    print(summaries)
    return summaries
