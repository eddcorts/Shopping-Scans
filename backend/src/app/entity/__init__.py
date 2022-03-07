from typing import Optional
from sqlmodel import SQLModel, Field

class BaseModel(SQLModel):
    id: Optional[int] = Field(primary_key=True)

from .Emitente import Emitente as Emitente