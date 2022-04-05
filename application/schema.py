from pydantic import BaseModel
from typing import Optional

class Symptom(BaseModel):
    fever: bool = False
    dry_cough: bool = False
    tiredness: bool = False
    breathing_problem: bool = False

class Parameter(BaseModel):
    image: str
    age  : Optional[int] = None
    sex  : Optional[str] = None