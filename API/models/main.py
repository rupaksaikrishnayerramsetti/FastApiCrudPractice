from typing import Optional
from pydantic import BaseModel

class Student(BaseModel):
    reg_id: Optional[int] = None
    name: str
    email: str
    branch: str
    section: str
    is_deleted: bool = False