import requests

class TokenManager:
    def __init__(self,base_url:str,username: str, password: str):
        self.base_url = base_url
        self.username = username
        self.password = password
        self._access_token = None
    
    def get_token(self) -> str:
        if not self._access_token:
            self._access_token = self._login()
        return self._access_token
    
    def _login(self) -> str:
        url = f"{self.base_url}/auth/login"

        payload = {
            "username": self.username,
            "password": self.password
        }

        response = requests.post(url, json=payload, timeout=10)

        if response.status_code != 200:
            raise RuntimeError(
                f"Login failed ({response.status_code}): {response.text}"
            )

        try:
            token = response.json().get("accessToken")
        except ValueError:
            raise RuntimeError("Login response is not valid JSON")

        if not token:
            raise RuntimeError("Token not found in response")

        return token
