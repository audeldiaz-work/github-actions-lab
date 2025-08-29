
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


@pytest.mark.parametrize(
    "item_id, q, expected",
    [
        (1, None, {"item_id": 1, "q": None}),
        (42, "test", {"item_id": 42, "q": "test"}),
        (0, "", {"item_id": 0, "q": ""}),
    ]
)
def test_read_item(item_id, q, expected):
    params = {}
    if q is not None:
        params["q"] = q
    response = client.get(f"/items/{item_id}", params=params)
    assert response.status_code == 200
    assert response.json() == expected


def test_read_item_invalid_id():
    response = client.get("/items/not-an-int")
    assert response.status_code == 422  # Unprocessable Entity for invalid int


def test_get_timestamp():
    response = client.get("/timestamp")
    assert response.status_code == 200
    data = response.json()
    assert "timestamp" in data
    # Check that the timestamp is a valid ISO format string
    from datetime import datetime
    try:
        datetime.fromisoformat(data["timestamp"])
    except ValueError:
        pytest.fail("Timestamp is not a valid ISO format string")
