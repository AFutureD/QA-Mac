from typing import Any
from pydantic import BaseModel, Field

class Model(BaseModel):
    metadata: dict[str, Any] = Field(default=dict(), exclude=True)

