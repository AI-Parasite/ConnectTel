from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_ticket_valid():
    payload = {
        "customer_id": 101,
        "subject": "Internet not working",
        "description": "My broadband connection has been down since morning.",
        "service_type": "broadband"
    }
    response = client.post("/tickets", json=payload)
    assert response.status_code == 201
    assert  response.json() == payload

def  test_create_ticket_invalid_customer_id():
    payload = {
        "customer_id": -5,
        "subject": "Internet not working",
        "description": "My broadband connection has been down since morning.",
        "service_type": "broadband"
        }
    response = client.post("/tickets", json=payload)
    assert response.status_code == 422

def test_create_ticket_invalid_subject_length():
    payload = {
        "customer_id": 101,
        "subject": "Net",
        "description": "My broadband connection has been down since morning.",
        "service_type": "broadband"
    }
    response = client.post("/tickets", json=payload)
    assert response.status_code == 422

def test_create_ticket_invalid_description_length():
    payload = {
        "customer_id": 101,
        "subject": "Internet not working",
        "description": "Down",
        "service_type": "broadband"
    }
    response = client.post("/tickets", json=payload)
    assert response.status_code == 422

def test_create_ticket_invalid_service_type():
    payload = {
        "customer_id": 101,
        "subject": "Internet not working",
        "description": "My broadband connection has been down since morning.",
        "service_type": "cable"
    }
    response = client.post("/tickets", json=payload)
    assert response.status_code == 422  

    