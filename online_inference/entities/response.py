from pydantic import BaseModel

class Response(BaseModel):
    id: int
    target: int
