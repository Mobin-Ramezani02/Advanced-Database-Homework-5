from fastapi import FastAPI
from router import myRouter
app = FastAPI()
app.include_router(myRouter)