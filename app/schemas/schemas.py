from pydantic import BaseModel, Field


class ReviewCreateSchema(BaseModel):
    review_by: str
    review_body: str
    rating: int | None = Field(gt=0, le=5)


class ReviewResponseSchema(ReviewCreateSchema):
    id: int
    book_id: int

