from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from redis import asyncio as aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from users.router import router as users_router
from works.router import router as works_router

app = FastAPI(
    title='Studio design api'
)


@app.get("/")
async def main():
    return {"message": "Hello World"}


app.include_router(users_router)
app.include_router(works_router)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    details = exc.errors()
    modified_details = []

    errors = {
        "status": "error",
        "message": details[0]["msg"],
        "data": None
    }

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder(errors),
    )


@app.on_event("startup")
async def on_startup() -> None:
    redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
