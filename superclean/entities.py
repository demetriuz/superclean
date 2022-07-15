from typing import Optional

from pydantic import BaseModel


class Node(BaseModel):
    id: Optional[int]
    value: str
    parent: Optional['Node'] = None
