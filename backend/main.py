from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel, Session, create_engine, select

from objects import Book

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)

@app.get("/books", response_model=List[Book])
async def get_books(is_archived: bool):
    with Session(engine) as session:
        # get all books if is_archived == True
        return session.exec(select(Book).where(is_archived == True or Book.is_archived == False)).all()

@app.post("/book")
async def add_book(book: Book) -> int | None:
    book.id = None # make sure data will not be overriden
    with Session(engine) as session:
        session.add(book)
        session.commit()
        session.refresh(book)
        return book.id