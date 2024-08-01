from datetime import datetime

from pydantic import BaseModel


class AddworkfromdisignerDTO(BaseModel):
    customer: str
    headline: str
    value: int
    designer_id: int


class WorkAllDTO(AddworkfromdisignerDTO):
    id: int
    design_is_agreed: bool = False
    value_is_agreed: bool = False
    date_of_payment: datetime


