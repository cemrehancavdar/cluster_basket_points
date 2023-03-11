import uvicorn
from fastapi import FastAPI

from python_basket_points.router import router

app = FastAPI(router=router)


def start():
    uvicorn.run("main:app", port=5000, log_level="info")
