from pydantic import BaseModel, Field

from api.models.category import Category
from api.models.tag import Tag


class Pet(BaseModel):
    id: int | None = None
    category: Category | None = None
    name: str | None = None
    photoUrls: list[str] = Field(default_factory=list)
    tags: list[Tag] = Field(default_factory=list)
    status: str | None = None
