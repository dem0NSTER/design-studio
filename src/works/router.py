from fastapi import APIRouter
from sqlalchemy import insert, select, and_

from database import session_maker
from works.models import Work
from works.schemas import AddWorkFromDisigner

router = APIRouter(
    prefix='/works',
    tags=['works'],
    responses={404: {'description': 'Not found'}}
)


@router.get('/')
async def index():
    return {'message': 'Hello World'}


@router.post('/add_work')
async def add_work(work: AddWorkFromDisigner):
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
            stmt = (
                select(Work)
                .where(and_(Work.designer_id == designer_id, Work.date_of_payment == None))
            )

            result = await session.execute(stmt)
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
