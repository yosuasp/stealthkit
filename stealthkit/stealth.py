import random
import requests
from fake_useragent import UserAgent

class StealthRequests:
    def __init__(self, proxies=None, browsers=None, os=None, use_cookies=False):
        self.session = requests.Session()
        self.ua = UserAgent(browsers=browsers or ['Chrome', 'Edge', 'Safari'], os=os or ['Windows', 'MacOS', 'Linux'])
        self.proxies = proxies or []
        self.use_cookies = use_cookies
    
    def get_headers(self):
        return {
            'User-Agent': self.ua.random,
            'Referer': random.choice([
                'https://google.com', 'https://bing.com', 'https://duckduckgo.com'
            ]),
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive'
        }
    
    def get_proxy(self):
        return random.choice(self.proxies) if self.proxies else None
    
    def request(self, method, url, **kwargs):
        proxy = self.get_proxy()
        headers = self.get_headers()
        kwargs.setdefault('headers', headers)
        if proxy:
            kwargs.setdefault('proxies', {'http': proxy, 'https': proxy})
        
        if not self.use_cookies:
            self.session.cookies.clear()
        
        return self.session.request(method, url, **kwargs)
    
    def get(self, url, **kwargs):
        return self.request('GET', url, **kwargs)
    
    def post(self, url, **kwargs):
        return self.request('POST', url, **kwargs)
    
    def close(self):
        self.session.close()

# Example Usage
stealth = StealthRequests(use_cookies=True)
resp = stealth.get("https://www.amazon.in")
print(resp.status_code)
