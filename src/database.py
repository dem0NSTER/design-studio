from typing import Annotated

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, mapped_column

from config import db_settings

URL_DB = db_settings.async_link_to_connect

engine = create_async_engine(url=URL_DB)
session_maker = async_sessionmaker(engine)

id = Annotated[int, mapped_column(primary_key=True)]


class Base(DeclarativeBase):
    repr_collums_count = 3

    def __repr__(self):
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            cols.append(f"{col}: {getattr(self, col)}")
            if idx >= self.repr_collums_count:
                break

        return f'<{self.__class__.__name__} {" ".join(cols)}>'
