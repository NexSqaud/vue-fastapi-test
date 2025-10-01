from sqlmodel import SQLModel, Field

class Book(SQLModel, table=True):
    __tablename__ = "books" # type: ignore

    id: int | None = Field(default = None, primary_key = True)
    name: str
    author: str
    release_year: int
    pages_count: int
    is_archived: bool
