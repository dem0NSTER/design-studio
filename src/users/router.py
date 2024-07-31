from fastapi import APIRouter
from users.schemas import Designer, Admin

router = APIRouter(
    prefix='/users',
    tags=['users'],
    responses={404: {'description': 'Not found'}}
)


@router.get('/')
async def index():
    return {'message': 'Hello World'}


@router.post('/add_designer')
async def add_designer(designer: Designer):
    pass


@router.post('/add_admin')
async def add_admin(admin: Admin):
    pass
