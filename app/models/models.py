from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class Review(Base):
    __tablename__ = 'reviews'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    movie_id: Mapped[int] = mapped_column(Integer, index=True)
    comment: Mapped[str]
    author: Mapped[str]
    rating: Mapped[int] = mapped_column(Integer, nullable=True)

