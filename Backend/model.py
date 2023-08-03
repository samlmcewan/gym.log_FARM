from pydantic import BaseModel

class Exercise(BaseModel):
    title: str
    description: str