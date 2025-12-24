
import requests
import time

from utils.logger import get_logger

BASE_URL = None

def send_request(method:str,endpoint:str,base_url:str):
    url = base_url + endpoint
    try:
        return requests.request(method, url)
    except requests.RequestException as exc:
        raise RuntimeError(f"HTTP request Failed: {exc}")


class HttpClient:
    def __init__(self, base_url: str, token_manager=None, max_retries=3, retry_delay=1):
        self.base_url = base_url
        self.token_manager = token_manager
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.logger = get_logger(self.__class__.__name__)

    def get(self, endpoint: str):
        url = self.base_url + endpoint
        headers = self._build_headers()

        for attempt in range(1, self.max_retries + 1):
            try:
                self.logger.info(f"GET {endpoint} (attempt {attempt})")
                response = requests.get(url, headers=headers, timeout=10)

                if response.status_code < 500:
                    return response

                self.logger.warning(
                    f"Server error {response.status_code}, retrying..."
                )
                time.sleep(self.retry_delay)

            except requests.RequestException as exc:
                self.logger.error(f"Request failed: {exc}")
                time.sleep(self.retry_delay)

        raise RuntimeError(f"GET {endpoint} failed after retries")

    def _build_headers(self) -> dict:
        headers = {}

        if self.token_manager:
            token = self.token_manager.get_token()
            headers["Authorization"] = f"Bearer {token}"

        return headers

    def _wait_before_retry(self, attempt, reason):
        if attempt == self.max_retries:
            return

        print(
            f"Retrying (attempt {attempt}/{self.max_retries}) "
            f"after failure: {reason}"
        )
        time.sleep(self.retry_delay)


