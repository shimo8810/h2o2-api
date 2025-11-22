from fastapi import APIRouter, FastAPI
from mangum import Mangum

from .routers import users

app = FastAPI()

api_v1 = APIRouter()
api_v1.include_router(users.router)


@api_v1.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello, World!!"}


app.include_router(api_v1, prefix="/api/v1")

handler = Mangum(app)
