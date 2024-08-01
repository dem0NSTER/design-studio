from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from datetime import date

from database import Base, id

from users.models import *


class Work(Base):
    __tablename__ = 'works'

    id: Mapped[id]
    customer: Mapped[str]
    headline: Mapped[str]
    value: Mapped[int]
    design_is_agreed: Mapped[bool | None]
    value_is_agreed: Mapped[bool | None]
    date_of_payment: Mapped[date | None]
    designer_id: Mapped[int] = mapped_column(ForeignKey('designers.id'))

    designer: Mapped["Designer"] = relationship(back_populates='works')
