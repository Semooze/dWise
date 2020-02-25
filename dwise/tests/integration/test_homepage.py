from starlette.testclient import TestClient
from dwise.main import app

def test_read_data():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200