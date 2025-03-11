from datetime import datetime
from pydantic import BaseModel


class GetExampleResponse(BaseModel):
    id: int
    name: str
    enabled: bool
    created_at: datetime
    updated_at: datetime


class PostExampleRequest(BaseModel):
    name: str


class DeleteExampleRequest(BaseModel):
    id: int
