from sqlalchemy.orm import Mapped, relationship

from database import Base, id

from works.models import *


class Admin(Base):
    __tablename__ = 'admins'

    id: Mapped[id]
    name: Mapped[str]
    is_main_admin: Mapped[bool] = mapped_column(default=False)


class Designer(Base):
    __tablename__ = 'designers'

    id: Mapped[id]
    name: Mapped[str]
    payment: Mapped[str]

    works: Mapped[list["Work"]] = relationship(back_populates='designer')
