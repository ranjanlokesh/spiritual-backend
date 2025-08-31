from sqlmodel import SQLModel, Field
from typing import Optional

class Reflection(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    insight: str