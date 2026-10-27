from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_ticket_valid():
    response = client.get("/tickets/42")
    assert response.status_code == 200
    assert response.json() == {"ticket_id": "CT-000042"}

def test_get_ticket_below_minimum_value():
    response = client.get("/tickets/0")
    assert response.status_code == 422

def test_get_ticket_over_maximum_value():
    response = client.get("/tickets/1000000")
    assert response.status_code == 422