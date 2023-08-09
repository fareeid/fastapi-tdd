# project/app/api/crud.py


from typing import Union

from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary


async def post(payload: SummaryPayloadSchema) -> int:
    # article_summary = generate_summary(payload.url)
    # summary = TextSummary(url=payload.url, summary=article_summary)
    summary = TextSummary(url=payload.url, summary="")
    await summary.save()
    return summary.id  # type: ignore


# async def post(payload: SummaryPayloadSchema) -> int:
#     summary = TextSummary(
#         url=payload.url,
#         summary="dummy summary",
#     )
#     await summary.save()
#     print(summary.id)  # type: ignore
#     return summary.id  # type: ignore


async def get(id: int) -> Union[dict, None]:
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary
    return None


async def get_all() -> list:
    summaries = await TextSummary.all().values()
    print(summaries)
    return summaries


async def delete(id: int) -> int:
    summary = await TextSummary.filter(id=id).first().delete()  # type: ignore
    return summary


async def put(id: int, payload: SummaryPayloadSchema) -> Union[dict, None]:
    summary = await TextSummary.filter(id=id).update(
        url=payload.url, summary=payload.summary  # type: ignore
    )
    if summary:
        updated_summary = await TextSummary.filter(id=id).first().values()
        return updated_summary
    return None
