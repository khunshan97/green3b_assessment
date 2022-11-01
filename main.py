from typing import List
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
import models
from database import SessionLocal

app = FastAPI()

class Author(BaseModel):
    id: int = None
    name: str

    class Config:
        orm_mode = True


class Book(BaseModel):
    id: int = None
    name: str
    author_id: int

    class Config:
        orm_mode = True


db = SessionLocal()


@app.get('/authors', response_model=List[Author], status_code=200, tags=['authors'])
def get_all_authors():
    authors = db.query(models.Author).all()

    return authors


@app.get('/authors/{author_id}', response_model=Author, status_code=status.HTTP_200_OK, tags=['authors'])
def get_an_author(author_id: int):
    author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if not author:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Author with id {author_id} not found')
    return author


@app.post('/authors', response_model=Author,
          status_code=status.HTTP_201_CREATED, tags=['authors'])
def create_an_author(author: Author):
    db_author = db.query(models.Author).filter(models.Author.name == author.name).first()

    if db_author is not None:
        raise HTTPException(status_code=400, detail="Author already exists")

    new_author = models.Author(
        name=author.name
    )

    db.add(new_author)
    db.commit()

    return new_author


@app.patch('/authors/{author_id}', response_model=Author, status_code=status.HTTP_200_OK, tags=['authors'])
def update_an_author(author_id: int, author: Author):
    author_to_update = db.query(models.Author).filter(models.Author.id == author_id).first()
    author_to_update.name = author.name

    db.commit()

    return author_to_update


@app.delete('/authors/{author_id}', tags=['authors'])
def delete_author(author_id: int):
    author_to_delete = db.query(models.Author).filter(models.Author.id == author_id).first()

    if author_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource Not Found")

    db.delete(author_to_delete)
    db.commit()

    return None


@app.get('/books', response_model=List[Book], status_code=200, tags=['books'])
def get_all_books():
    books = db.query(models.Book).all()

    return books


@app.get('/books/{book_id}', response_model=Book, status_code=status.HTTP_200_OK, tags=['books'])
def get_a_book(book_id: int):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Book with id {book_id} not found')
    return book


@app.post('/books', response_model=Book,
          status_code=status.HTTP_201_CREATED, tags=['books'])
def create_a_book(book: Book):
    db_book = db.query(models.Book).filter(models.Book.name == book.name).first()

    if db_book is not None:
        raise HTTPException(status_code=400, detail="Book already exists")

    new_book = models.Book(
        name=book.name,
        author_id=book.author_id
    )

    db.add(new_book)
    db.commit()

    return new_book


@app.patch('/books/{book_id}', response_model=Book, status_code=status.HTTP_200_OK, tags=['books'])
def update_a_book(book_id: int, book: Book):
    book_to_update = db.query(models.Book).filter(models.Book.id == book_id).first()
    book_to_update.name = book.name
    book_to_update.author_id = book.author_id

    db.commit()

    return book_to_update


@app.delete('/books/{book_id}', tags=['books'])
def delete_book(book_id: int):
    book_to_delete = db.query(models.Book).filter(models.Book.id == book_id).first()

    if book_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource Not Found")

    db.delete(book_to_delete)
    db.commit()

    return None


@app.get('/authors/{author_id}/books', response_model=List[Book], status_code=status.HTTP_200_OK, tags=['authors'])
def get_author_books(author_id: int):
    books = db.query(models.Book).filter(models.Book.author_id == author_id).all()
    return books
