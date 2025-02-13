import random
import requests
from fake_useragent import UserAgent

class StealthRequests:
    def __init__(self, use_cookies=False, browsers=None, os=None):
        self.session = requests.Session()
        try:
            self.ua = UserAgent(browsers=browsers or ['Chrome', 'Edge', 'Safari'], os=os or ['Windows', 'MacOS', 'Linux'])
        except:
            self.ua = None  # Fallback in case fake_useragent fails
        self.proxies = []
        self.use_cookies = use_cookies
        self.headers = {
            'User-Agent': self.ua.random if self.ua else "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            'Referer': random.choice(['https://google.com', 'https://bing.com', 'https://duckduckgo.com']),
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive'
        }
    
    def set_headers(self, user_agent=None, referer=None):
        self.headers['User-Agent'] = user_agent or (self.ua.random if self.ua else self.headers['User-Agent'])
        self.headers['Referer'] = referer or self.headers['Referer']
    
    def set_proxies(self, proxies):
        self.proxies = proxies
    
    def get_proxy(self):
        return random.choice(self.proxies) if self.proxies else None
    
    def request(self, method, url, retries=3, timeout=10, **kwargs):
        for _ in range(retries):
            proxy = self.get_proxy()
            kwargs.setdefault('headers', self.headers)
            
            if proxy:
                kwargs.setdefault('proxies', {'http': proxy, 'https': proxy})
            
            if not self.use_cookies:
                self.session.cookies.clear()
            
            try:
                return self.session.request(method, url, timeout=timeout, **kwargs)
            except requests.RequestException as e:
                print(f"Request failed: {e}, Retrying...")
        return None
    
    def get(self, url, **kwargs):
        return self.request('GET', url, **kwargs)
    
    def post(self, url, **kwargs):
        return self.request('POST', url, **kwargs)
    
    def close(self):
        self.session.close()

# Example Usage
stealth = StealthRequests(use_cookies=True, browsers=['Chrome', 'Firefox'], os=['Windows', 'Linux'])
stealth.set_proxies(["http://103.57.70.231:39143"])
stealth.set_headers(referer="https://example.com")
resp = stealth.get("https://example.com")
if resp:
    print(resp.status_code)
