from fastapi import APIRouter
from sqlalchemy import insert, delete
from sqlalchemy import select

from database import session_maker
from users.models import Designer, Admin
from users.schemas import DesignerDTO, AdminDTO
from utils import ApiException, check_admin, AdminNotMain, check_designer

router = APIRouter(
    prefix='/users',
    tags=['users'],
    responses={404: {'description': 'Not found'}}
)


@router.get('/')
async def index():
    return {'message': 'router for work with users'}


@router.get('/select_all_users')
async def select_all_users():
    try:
        async with session_maker() as session:
            query = (
                select(Admin.id)
            )
            admins = await session.execute(query)

            query = (
                select(Designer.id)
            )
            designers = await session.execute(query)

            result_admins = admins.scalars().all()
            result_designers = designers.scalars().all()

            result = {
                'admins': result_admins,
                'designers': result_designers
            }

            response = {
                'status': 'success',
                'message': None,
                'data': result
            }
            return response

    except Exception as e:
        response = {
            'status': 'error',
            'message': str(e),
            'data': None
        }
        return response


@router.post('/add_designer')
async def add_designer(designer: DesignerDTO, admin_id: int):
    try:
        async with session_maker() as session:
            await check_admin(admin_id, session)

            stmt = (
                insert(Designer)
                .values(**designer.dict())
            )

            await session.execute(stmt)
            await session.commit()

            response = {
                'status': 'success',
                'message': None,
                'data': designer
            }

            return response

    except ApiException as e:
        response = {
            'status': 'error',
            'message': str(e),
            'data': None
        }
        return response

    except Exception as e:
        response = {
            'status': 'error',
            'message': str(e),
            'data': None
        }

        return response


@router.post('/delete_designer')
async def delete_designer(designer_id: int, admin_id: int):
    try:
        async with session_maker() as session:
            await check_admin(admin_id, session)
            await check_designer(designer_id, session)

            query = (
                select(Designer)
                .where(Designer.id == designer_id)
            )

            result = await session.execute(query)
            designer = result.scalars().first()

            stmt = (
                delete(Designer)
                .where(Designer.id == designer_id)
            )
            await session.execute(stmt)
            await session.commit()

            response = {
                'status': 'success',
                'message': f'designer {designer.name} deleted',
                'data': None
            }

            return response

    except ApiException as e:
        response = {
            'status': 'error',
            'message': str(e),
            'data': None
        }

        return response

    except Exception as e:
        response = {
            'status': 'error',
            'message': str(e),
            'data': None
        }

        return response


@router.post('/add_admin')
async def add_admin(new_admin: AdminDTO, id_main_admin: int):
    try:
        async with session_maker() as session:
            admin = await check_admin(id_main_admin, session)

            if admin.is_main_admin is False:
                raise AdminNotMain

            new_admin.is_main_admin = False

            stmt = (
                insert(Admin)
                .values(**new_admin.dict())
            )

            await session.execute(stmt)
            await session.commit()

            response = {
                'status': 'success',
                'message': f'new admin {new_admin.name} added',
                'data': None
            }

            return response

    except ApiException as e:
        response = {
            'status': 'error',
            'message': str(e),
            'data': None
        }

        return response

    except Exception as e:
        response = {
            'status': 'error',
            'message': str(e),
            'data': None
        }

        return response


@router.post('/delete_admin')
async def delete_admin(admin_id: int, id_main_admin: int):
    try:
        async with session_maker() as session:
            await check_admin(admin_id, session)
            admin = await check_admin(id_main_admin, session)
            if admin.is_main_admin is False:
                raise AdminNotMain

            stmt = (
                delete(Admin)
                .where(Admin.id == admin_id)
            )
            await session.execute(stmt)
            await session.commit()

            response = {
                'status': 'success',
                'message': 'admin deleted',
                'data': None
            }
            return response

    except ApiException as e:
        response = {
            'status': 'error',
            'message': str(e),
            'data': None
        }
        return response

    except Exception as e:
        print(e)
        response = {
            'status': 'error',
            'message': 'server error',
            'data': None
        }

        return response
