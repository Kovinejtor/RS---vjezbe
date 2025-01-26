from fastapi import FastAPI, APIRouter
from routers import filmovi

app = FastAPI()

app.include_router(filmovi.router) 
