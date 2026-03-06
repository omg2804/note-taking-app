import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Note Taking App!"}


def test_create_note():
    response = client.post("/notes/", json={"title": "Test Note", "content": "This is a test note."})
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["title"] == "Test Note"


def test_list_notes():
    response = client.get("/notes/")
    assert response.status_code == 200
    assert "notes" in response.json()


def test_get_note():
    response = client.post("/notes/", json={"title": "Another Note", "content": "This is another test note."})
    note_id = response.json()["id"]
    response = client.get(f"/notes/{note_id}")
    assert response.status_code == 200
    assert response.json()["id"] == note_id


def test_update_note():
    response = client.post("/notes/", json={"title": "Note to Update", "content": "Content to update."})
    note_id = response.json()["id"]
    response = client.put(f"/notes/{note_id}", json={"title": "Updated Note"})
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Note"


def test_delete_note():
    response = client.post("/notes/", json={"title": "Note to Delete", "content": "This note will be deleted."})
    note_id = response.json()["id"]
    response = client.delete(f"/notes/{note_id}")
    assert response.status_code == 200
    assert response.json()["id"] == note_id

    response = client.get(f"/notes/{note_id}")
    assert response.status_code == 404