import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from .conftest import Utils


@pytest.fixture(scope="function")
def client(api_app: FastAPI) -> TestClient:
    print("Create client fixture")
    return TestClient(api_app)


def test_api(client: TestClient) -> None:
    print(f"Execute {test_api.__name__}")
    response = client.get("/items/123", params={"q": "foo"})
    assert response.status_code == 200
    assert response.json() == {"item_id": 123, "q": "foo"}


def test_api_2(client: TestClient) -> None:
    print(f"Execute {test_api_2.__name__}")
    response = client.get("/items/124", params={"q": "bar"})
    assert response.status_code == 200
    assert response.json() == {"item_id": 124, "q": "bar"}


def test_use_shared_helpers(test_utils: Utils) -> None:
    print(test_utils.super_useful_helper())
    assert True
