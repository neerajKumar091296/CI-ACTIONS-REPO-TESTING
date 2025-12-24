

import pytest
from auth.token_manager import TokenManager
from Client.http_client import HttpClient

BASE_URL = "https://dummyjson.com"


@pytest.fixture
def token_manager():
    return TokenManager(
        base_url=BASE_URL,
        username="emilys",
        password="emilyspass"
    )

@pytest.fixture
def auth_client(token_manager):
    return HttpClient(
        base_url=BASE_URL,
        token_manager=token_manager
    )