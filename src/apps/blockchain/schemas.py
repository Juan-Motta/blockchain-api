from pydantic import BaseModel
from datetime import datetime


class BlockSchema(BaseModel):
    index: int
    timestamp: datetime
    proof: int
    previous_hash: str
    data: dict | None
