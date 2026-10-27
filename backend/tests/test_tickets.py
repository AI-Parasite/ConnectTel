import pytest
from app.tickets import create_ticket_id


def test_ticket_id_valid():
    assert create_ticket_id(42) == "CT-000042"

def test_ticket_id_maximum():
    assert create_ticket_id(999999) == "CT-999999"   

def test_ticket_id_zero():
    with pytest.raises(ValueError):
        create_ticket_id(0)

def test_ticket_id_negative():
    with pytest.raises(ValueError):
        create_ticket_id(-1)

def test_ticket_id_exceeding_max():
    with pytest.raises(ValueError):
        create_ticket_id(1000000)

def test_ticket_id_non_integer():
    with pytest.raises(TypeError):
        create_ticket_id("string")

def test_ticket_id_boolean():
    with pytest.raises(TypeError):
        create_ticket_id(True)
