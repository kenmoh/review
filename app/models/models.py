from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class Review(Base):
    __tablename__ = 'reviews'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    book_id: Mapped[int] = mapped_column(Integer, index=True)
    review_body: Mapped[str]
    review_by: Mapped[str]
    rating: Mapped[int] = mapped_column(Integer, nullable=True)

