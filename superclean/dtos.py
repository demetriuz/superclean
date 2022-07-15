from typing import Optional

from pydantic import BaseModel


class CreateRequestNodeDTO(BaseModel):
    value: str
    parent_id: Optional[int]


class ResponseNodeDTO(BaseModel):
    id: int
    value: str
    parent_id: Optional[int]
