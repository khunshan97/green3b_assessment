from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    books = relationship('Book', back_populates='author')

    def __repr__(self):
        return f"<Author name={self.name}>"


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship('Author', back_populates='books')

    def __repr__(self):
        return f"<Book name={self.name}>"
