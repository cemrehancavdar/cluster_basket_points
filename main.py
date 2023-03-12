import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from python_basket_points.router import router

app = FastAPI()
app.include_router(router=router)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def start():
    uvicorn.run("main:app", port=5000, log_level="info", reload=True)
