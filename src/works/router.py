import datetime

from fastapi import APIRouter
from sqlalchemy import insert, select, and_, update

from database import session_maker
from works.models import Work
from works.schemas import AddworkfromdisignerDTO

router = APIRouter(
    prefix='/works',
    tags=['works'],
    responses={404: {'description': 'Not found'}}
)


@router.get('/')
async def index():
    return {'message': 'Hello World'}


@router.post('/add_work')
async def add_work(work: AddworkfromdisignerDTO):
    try:
        async with session_maker() as session:
            stmt = (
                insert(Work)
                .values(**work.dict())
            )
            await session.execute(stmt)
            await session.commit()

        response = {
            'status': 'success',
            'message': None,
            'data': work
        }

        return response

    except Exception as e:
        response = {'status': 'error', 'message': str(e), 'data': None}
        return response


@router.get('/get_works')
async def get_works(designer_id: int):
    try:
        async with session_maker() as session:
            query = (
                select(Work)
                .where(and_(Work.designer_id == designer_id, Work.date_of_payment == None))
            )

            result = await session.execute(query)
            works = result.scalars().all()

        response = {
            'status': 'success',
            'message': None,
            'data': works
        }

        return response

    except Exception as e:
        print(e)

        response = {
            'status': 'error',
            'message': str(e),
            'data': None
        }

        return response


@router.post('/set_date_of_payment')
async def set_date_of_payment(work_id: int):
    try:
        async with session_maker() as session:
            stmt = (
                update(Work)
                .where(Work.id == work_id)
                .values(date_of_payment=datetime.date.today())
            )
            await session.execute(stmt)
            await session.commit()

        response = {
            'status': 'success',
            'message': None,
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
