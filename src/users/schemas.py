from pydantic import BaseModel
from works.schemas import WorkAllDTO


class AdminDTO(BaseModel):
    id: int
    name: str
    is_main_admin: bool = False


class DesignerDTO(BaseModel):
    id: int
    name: str
    payment: str


class DesingerWithWorksDTO(DesignerDTO):
    works: list["WorkAllDTO"]
