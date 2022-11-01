from fastapi.testclient import TestClient
from database import Base, engine

from main import app

client = TestClient(app)
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(engine)

author_name = "First Author"
updated_author_name = "Updated Author"

book_name = "First Book"
updated_book_name = "Updated Book"


def test_create_author():
    response = client.post(
        "/authors",
        json={
            "name": author_name
        }
    )
    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "name": author_name
    }


def test_create_author_with_existing_name():
    response = client.post(
        "/authors",
        json={
            "name": author_name
        }
    )
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Author already exists"
    }


def test_get_all_authors():
    response = client.get("/authors")
    assert response.status_code == 200
    assert response.json() == [{
        "id": 1,
        "name": author_name
    }]


def test_get_author():
    response = client.get("/authors/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": author_name
    }


def test_update_author():
    response = client.patch(
        "/authors/1",
        json={
            "name": updated_author_name
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": updated_author_name
    }


def test_delete_author():
    response = client.delete("/authors/1")
    assert response.status_code == 200
    assert response.json() is None


def test_get_author_after_deletion():
    response = client.get("/authors/1")
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Author with id 1 not found"
    }


def test_get_all_authors_after_deletion():
    response = client.get("/authors")
    assert response.status_code == 200
    assert response.json() == []


def test_create_author_again():
    response = client.post(
        "/authors",
        json={
            "name": author_name
        }
    )
    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "name": author_name
    }


def test_create_book():
    response = client.post(
        "/books",
        json={
            "name": book_name,
            "author_id": 1
        }
    )
    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "name": book_name,
        "author_id": 1
    }


def test_create_book_with_existing_name():
    response = client.post(
        "/books",
        json={
            "name": book_name,
            "author_id": 1
        }
    )
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Book already exists"
    }


def test_get_book():
    response = client.get("/books/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": book_name,
        "author_id": 1
    }


def test_get_all_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert response.json() == [{
        "id": 1,
        "name": book_name,
        "author_id": 1
    }]


def test_get_books_by_author():
    response = client.get("/authors/1/books")
    assert response.status_code == 200
    assert response.json() == [{
        "id": 1,
        "name": book_name,
        "author_id": 1
    }]


def test_update_book():
    response = client.patch(
        "/books/1",
        json={
            "name": updated_book_name,
            "author_id": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": updated_book_name,
        "author_id": 1
    }


def test_delete_book():
    # raise Exception("Not implemented")
    response = client.delete("/books/1")
    assert response.status_code == 200
    assert response.json() is None


def test_get_book_after_deletion():
    response = client.get("/books/1")
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Book with id 1 not found"
    }


def test_get_all_books_after_deletion():
    response = client.get("/books")
    assert response.status_code == 200
    assert response.json() == []
