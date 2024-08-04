import datetime

from fastapi import APIRouter
from sqlalchemy import insert, select, and_, update, delete

from database import session_maker
from utils import check_designer, ApiException, check_work
from works.models import Work
from works.schemas import AddworkfromdisignerDTO

router = APIRouter(
    prefix='/works',
    tags=['works'],
    responses={404: {'description': 'Not found'}}
)


@router.get('/')
async def index():
    return {'message': 'router for work with "works"'}


@router.post('/add_work')
async def add_work(work: AddworkfromdisignerDTO):
    try:
        async with session_maker() as session:
            await check_designer(work.designer_id, session)

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


@router.post('/delete_work')
async def delete_work(work_id: int):
    try:
        async with session_maker() as session:
            await check_work(work_id, session)

            stmt = (
                delete(Work)
                .where(Work.id == work_id)
            )
            await session.execute(stmt)
            await session.commit()

        response = {
            'status': 'success',
            'message': None,
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


@router.post('/get_works')
async def get_works(designer_id: int):
    try:
        async with session_maker() as session:
            await check_designer(designer_id, session)

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
            'message': str(e),
            'data': None
        }

        return response


@router.post('/set_date_of_payment')
async def set_date_of_payment(work_id: int):
    try:
        async with session_maker() as session:
            await check_work(work_id, session)

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


@router.post('set_design_is_agreed')
async def set_design_is_agree(work_id: int):
    try:
        async with session_maker() as session:
            await check_work(work_id, session)

            stmt = (
                update(Work)
                .where(Work.id == work_id)
                .values(design_is_agreed=True)
            )
            await session.execute(stmt)
            await session.commit()

            response = {
                'status': 'success',
                'message': 'data updated',
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


@router.post('set_value_is_agreed')
async def set_value_is_agree(work_id: int):
    try:
        async with session_maker() as session:
            await check_work(work_id, session)

            stmt = (
                update(Work)
                .where(Work.id == work_id)
                .values(value_is_agreed=True)
            )
            await session.execute(stmt)
            await session.commit()

            response = {
                'status': 'success',
                'message': 'data updated',
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
