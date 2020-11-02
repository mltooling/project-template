from fastapi.testclient import TestClient

from template_package.api import app

client = TestClient(app)


def test_api() -> None:
    response = client.get("/items/123", params={"q": "foo"})
    assert response.status_code == 200
    assert response.json() == {"item_id": 123, "q": "foo"}
