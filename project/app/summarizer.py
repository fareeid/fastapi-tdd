# project/app/summarizer.py

# import asyncio
import nltk  # type: ignore
from newspaper import Article  # type: ignore

# from pydantic import AnyHttpUrl
from app.models.tortoise import TextSummary


# def generate_summary(url: str) -> str:
#     article = Article(url)
#     article.download()
#     article.parse()

#     try:
#         nltk.data.find("tokenizers/punkt")
#     except LookupError:
#         nltk.download("punkt")
#     finally:
#         article.nlp()

#     return article.summary


async def generate_summary(summary_id: int, url: str) -> None:
    article = Article(url)
    article.download()
    article.parse()

    try:
        nltk.data.find("tokenizers/punkt")
    except LookupError:
        nltk.download("punkt")
    finally:
        article.nlp()

    summary = article.summary

    # await asyncio.sleep(10)

    await TextSummary.filter(id=summary_id).update(summary=summary)
