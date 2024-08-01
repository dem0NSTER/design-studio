from fastapi import APIRouter
from sqlalchemy import insert

from users.schemas import DesignerDTO, AdminDTO
from database import session_maker
from users.models import Designer

router = APIRouter(
    prefix='/users',
    tags=['users'],
    responses={404: {'description': 'Not found'}}
)


@router.get('/')
async def index():
    return {'message': 'Hello World'}


@router.post('/add_designer')
async def add_designer(designer: DesignerDTO):
    try:
        async with session_maker() as session:
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
    except Exception as e:
        response = {
            'status': 'error',
            'message': str(e),
            'data': None
        }

        return response


@router.post('/add_admin')
async def add_admin(admin: AdminDTO):
    pass
