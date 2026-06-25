from pydantic import BaseModel


class Tag(BaseModel):
    id: int | None = None
    name: str | None = None
