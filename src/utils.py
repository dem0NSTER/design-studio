from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from users.models import Admin, Designer
from works.models import Work


async def check_work(work_id: int, session: AsyncSession) -> Work:
    """
    type work_id: int
    rtype: bool
    """
    query = (
        select(Work)
        .where(Work.id == work_id)
    )
    result = await session.execute(query)
    work = result.scalars().first()
    if work is None:
        raise WorkNotFound
    return work


async def check_designer(designer_id: int, session: AsyncSession) -> Designer:
    """
    type designer_id: int
    rtype: bool
    """
    query = (
        select(Designer)
        .where(Designer.id == designer_id)
    )
    result = await session.execute(query)
    designer = result.scalars().first()
    if designer is None:
        raise DesignerNotFound
    return designer


async def check_admin(admin_id: int, session: AsyncSession) -> Admin:
    """
    type admin_id: int
    rtype: bool
    """
    query = (
        select(Admin)
        .where(Admin.id == admin_id)
    )
    result = await session.execute(query)
    admin = result.scalars().first()
    if admin is None:
        raise AdminNotFound
    return admin


def write_log(e: str, __name_: str, func_name: str) -> None:
    """
    type e: str (exeption)
    type __name_: str (__name__)
    type func_name: str
    rtype: None
    """
    with open("log.txt", "a") as file:
        file.write(f"{datetime.utcnow().strftime('%Y-%m-%d %H:%M')}: (func: {__name_}: {func_name}) {e};\n\n")


class ApiException(Exception):
    pass


class AdminNotFound(ApiException):
    def __str__(self):
        return "admin not found"


class DesignerNotFound(ApiException):
    def __str__(self):
        return "designer not found"


class AdminNotMain(ApiException):
    def __str__(self):
        return "admin is not main"


class WorkNotFound(ApiException):
    def __str__(self):
        return "work not found"
