from fastapi import APIRouter, status,  Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.schemas import ReviewResponseSchema, ReviewCreateSchema
from app.services import services


review_router = APIRouter(prefix='/api/reviews', tags=['Review'])


@review_router.get('', status_code=status.HTTP_200_OK)
def get_reviews(db: Session = Depends(get_db)) -> list[ReviewResponseSchema]:
    return services.get_all_reviews(db)


@review_router.post('/{book_id}', status_code=status.HTTP_201_CREATED)
def add_review(book_id, review: ReviewCreateSchema, db: Session = Depends(get_db)) -> ReviewResponseSchema:
    return services.add_new_review(book_id, review, db)


@review_router.get('/{book_id}', status_code=status.HTTP_200_OK)
def get_book_reviews(book_id: int, db: Session = Depends(get_db)) -> list[ReviewResponseSchema]:
    return services.get_all_reviews_by_book(book_id, db)


@review_router.get('/average-rating/{book_id}', status_code=status.HTTP_200_OK)
def get_book_avg_rating(book_id: int, db: Session = Depends(get_db)) -> float:
    return services.get_average_rating_by_book(book_id, db)


@review_router.delete('/delete-reviews/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_book_reviews(book_id: int, db: Session = Depends(get_db)):
    return services.delete_book_reviews(book_id, db)