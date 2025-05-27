import curl_cffi.requests as requests
import random
import time
from fake_useragent import UserAgent

class StealthSession:
    def __init__(self, proxies=None, retries=3, enable_logging=False):
        self.session = requests.Session()
        self.retries = retries
        self.enable_logging = enable_logging
        self.user_agent = UserAgent()
        self.default_headers = {
            "User-Agent": UserAgent(browsers=['Chrome'], os=['Windows', 'MacOS', 'Linux']).random,
            "Referer": self._get_random_referer(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        }
        self.session.headers.update(self.default_headers)
        self.proxies = proxies
        self.cookies = None

        # Configure impersonate - this is specific to curl_cffi
        self.session.impersonate = "chrome110"

    def _get_random_referer(self):
        referers = [
            "https://www.google.com/",
            "https://www.bing.com/",
            "https://www.yahoo.com/",
            "https://duckduckgo.com/"
        ]
        return random.choice(referers)

    def set_headers(self, additional_headers):
        self.session.headers.update(additional_headers)

    def fetch_cookies(self, base_url):
        response = self.session.get(base_url, proxies=self.proxies, headers=self.default_headers)
        if response.status_code == 200:
            self.cookies = dict(response.cookies)
            self.session.cookies.update(self.cookies)

    def clear_cookies(self):
        self.session.cookies.clear()
        self.cookies = None

    def request(self, method, url, **kwargs):
        if self.proxies:
            kwargs["proxies"] = self.proxies

        for _ in range(self.retries):
            try:
                if self.enable_logging:
                    print(f"[INFO] Requesting {method.upper()} {url}...")

                start_time = time.time()
                response = self.session.request(method, url, **kwargs)
                elapsed = time.time() - start_time

                if self.enable_logging:
                    print(f"[INFO] Status Code: {response.status_code} | Time: {elapsed:.2f}s")

                return response
            except requests.RequestException as e:
                if self.enable_logging:
                    print(f"[ERROR] Request failed: {e}")
                continue
        return None

    def get(self, url, **kwargs):
        return self.request("GET", url, **kwargs)

    def post(self, url, **kwargs):
        return self.request("POST", url, **kwargs)

    def put(self, url, **kwargs):
        return self.request("PUT", url, **kwargs)

    def delete(self, url, **kwargs):
        return self.request("DELETE", url, **kwargs)

if __name__ == "__main__":
    sr = StealthSession(enable_logging=True)
    nse_url = "https://www.nseindia.com/api/corporates-pit?index=equities"

    custom_headers = {
        "Referer": "https://www.nseindia.com",
        "Accept": "application/json",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "method": "GET",
        "path": "/api/corporates-pit?",
        "scheme": "https",
    }

    sr.set_headers(custom_headers)
    sr.fetch_cookies("https://www.nseindia.com/companies-listing/corporate-filings-insider-trading")
    response = sr.get(nse_url)
    print(sr.session.cookies)
    print(response.text)

    """
    if response:
        print(response.json())  # Print stock data as JSON
    else:
        print("Failed to fetch stock data")
    """
