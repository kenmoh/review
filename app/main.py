from fastapi import FastAPI, status

from app.models import models
from app.database import database
from app.routers import routers
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title='Review API', description='A review API for book to demonstrate Microservices')


@app.get('/')
async def health_check():
    return {'health_status': status.HTTP_200_OK}


app.include_router(routers.review_router)