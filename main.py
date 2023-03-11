import uvicorn
from fastapi import FastAPI

from python_basket_points.router import router

app = FastAPI()
app.include_router(router=router)


def start():
    uvicorn.run("main:app", port=5000, log_level="info", reload=True)
