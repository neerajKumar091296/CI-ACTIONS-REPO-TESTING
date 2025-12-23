
import requests

BASE_URL = None

def send_request(method:str,endpoint:str,base_url:str):
    url = base_url + endpoint
    try:
        return requests.request(method, url)
    except requests.RequestException as exc:
        raise RuntimeError(f"HTTP request Failed: {exc}")
