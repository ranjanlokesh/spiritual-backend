from sqlmodel import SQLModel, Field
from typing import Optional

class Reflection(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    insight: str

class AIReflection(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    prompt: str
    response: str

class AIReflectionCreate(SQLModel):
    prompt: str
    response: str
