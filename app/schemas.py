from pydantic import BaseModel, Field


class PostCreateUpdate(BaseModel):
    title: str = Field(..., max_length=100)
    description: str = Field(..., max_length=500)
