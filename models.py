from db import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import TEXT

from datetime import datetime


class NoteModel(Base):
    __tablename__ = "notes"
    id: Mapped[str] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(TEXT, nullable=False)
    date_created: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Note {self.title} at {self.date_created}>"
