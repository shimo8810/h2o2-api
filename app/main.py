from fastapi import FastAPI
from mangum import Mangum

from .routers import users

app = FastAPI()
app.include_router(users.router)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello, World!!"}


handler = Mangum(app)
