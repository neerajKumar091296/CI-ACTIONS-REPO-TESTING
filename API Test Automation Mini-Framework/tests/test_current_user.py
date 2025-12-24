from auth.token_manager import TokenManager
from Client.http_client import HttpClient

BASE_URL = "https://dummyjson.com"

def test_get_current_user(auth_client):

    response = auth_client.get("/auth/me")

    assert response.status_code == 200
    assert response.json()["username"] == "emilys"
