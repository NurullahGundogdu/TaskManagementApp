from pydantic import BaseModel


class Task(BaseModel):
    id: str
    title: str
    status: str
    description: str
    created_at: str
    updated_at: str

