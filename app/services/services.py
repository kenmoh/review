from fastapi import HTTPException, status

from app.models.models import Review
from app.database.database import session
from app.schemas.schemas import ReviewCreateSchema


def get_all_reviews(db: session):
    try:
        return db.query(Review).all()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


def add_new_review(movie_id: int, review: ReviewCreateSchema, db: session):
    try:
        with session.begin():

            new_review = Review(
                movie_id=movie_id,
                author=review.author,
                comment=review.comment,
                rating=review.rating
            )
            db.add(new_review)
            db.commit()
            db.refresh(new_review)

            return new_review
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


def get_all_reviews_by_movie(movie_id, db: session):
    try:
        return db.query(Review).filter(Review.movie_id == movie_id).all()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


def get_average_rating_by_movie(movie_id, db: session):
    try:

        ratings = db.query(Review).filter(Review.movie_id == movie_id).all()
        if len(ratings) > 0:
            return sum([rating.rating for rating in ratings]) / len(ratings)
        return 0
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


def delete_movie_reviews(movie_id: int, db: session):
    db_movie_reviews = db.query(Review).filter(Review.movie_id == movie_id).all()

    if not db_movie_reviews:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Book with ID: {movie_id} not found!')
    for db_movie_review in db_movie_reviews:
        db.delete(db_movie_review)
        db.commit()
