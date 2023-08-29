from fastapi import HTTPException, status

from app.models.models import Review
from app.database.database import session
from app.schemas.schemas import ReviewCreateSchema


def get_all_reviews(db: session):
    try:
        return db.query(Review).all()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


def add_new_review(book_id: int, review: ReviewCreateSchema, db: session):
    try:
        with session.begin():

            new_review = Review(
                book_id=book_id,
                review_body=review.review_body,
                review_by=review.review_by,
                rating=review.rating
            )
            db.add(new_review)
            db.commit()
            db.refresh(new_review)

            return new_review
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


def get_all_reviews_by_book(book_id, db: session):
    try:
        return db.query(Review).filter(Review.book_id == book_id).all()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


def get_average_rating_by_book(book_id, db: session):
    try:

        ratings = db.query(Review).filter(Review.book_id == book_id).all()
        if len(ratings) > 0:
            return sum([rating.rating for rating in ratings]) / len(ratings)
        return 0
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


def delete_book_reviews(book_id: int, db: session):
    db_book_reviews = db.query(Review).filter(Review.book_id == book_id).all()

    if not db_book_reviews:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Book with ID: {book_id} not found!')
    db.delete(db_book_reviews)
    db.commit()
