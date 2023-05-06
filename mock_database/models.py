from enum import Enum
from typing import List
from pydantic import BaseModel

class Languages(str, Enum):
    b = "b"
    c = "c"
    java = "java"
    javascript = "javascript"
    python = "python"

class Programmer(BaseModel):
    id: int
    name: str
    age: int
    languages: List[Languages]


