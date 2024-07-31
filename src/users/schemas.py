from pydantic import BaseModel
from works.schemas import WorkAll


class Admin(BaseModel):
    id: int
    name: str
    is_main_admin: bool = False


class Designer(BaseModel):
    id: int
    name: str
    payment: str


class DesingerWithWorks(Designer):
    works: list["WorkAll"]
