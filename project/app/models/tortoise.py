# project/app/models/tortoise.py

from datetime import datetime
from tortoise import fields, models

# from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel


class TextSummary(models.Model):
    url = fields.TextField()
    summary = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.url


class SummarySchema(BaseModel):
    id: int
    url: str
    summary: str
    created_at: datetime

    class Config:
        from_attributes = True


# SummarySchema = pydantic_model_creator(TextSummary)
