from starlette.testclient import TestClient
from dwise.main import app

def test_home_page():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200

def test_filter_page():
    with TestClient(app) as client:
        response = client.get("/data?keyword=2")
        assert response.status_code == 200
        response = client.get("/data?no=2")
        assert response.status_code == 422