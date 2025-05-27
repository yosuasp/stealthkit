# StealthKit

## Overview

`StealthKit` is a Python module that provides a stealthy session handler for web scraping and automated requests. It mimics real user behavior by rotating user agents, setting referers, handling cookies, managing proxies, and implementing retry logic.

## Features

- **User-Agent Rotation**: Automatically rotates user agents from Chrome, Edge, and Safari across different OS platforms (Windows, MacOS, Linux).
- **Random Referer Selection**: Simulates real browsing behavior by sending requests with randomized referers from search engines.
- **Cookie Handling**: Fetches and stores cookies from specified URLs to maintain session persistence.
- **Proxy Support**: Allows requests to be routed through a provided proxy.
- **Retry Logic**: Retries failed requests up to three times before giving up.
- **RESTful Requests**: Supports GET, POST, PUT, and DELETE methods with automatic proxy integration.

## Installation

```sh
pip install stealthkit
```

## Basic Usage

```python
from stealthkit import StealthSession

# Create a stealth session
sr = StealthSession()

# Fetch cookies from a base URL
sr.fetch_cookies("https://www.example.com")

# Make a GET request
response = sr.get("https://www.example.com/api")

# Print the response JSON if successful
if response:
    print(response.json())
else:
    print("Failed to fetch data")
```

## Advanced Usage

### 1. Custom Headers
```python
custom_headers = {
    "Referer": "https://www.example.com",
    "Accept": "application/json",
}
sr.set_headers(custom_headers)
```

### 2. Using Proxies
```python
proxies = {"http": "http://proxy.example.com:8080", "https": "https://proxy.example.com:8080"}
sr = StealthSession(proxies=proxies)
```

### 3. Retries
```python
sr = StealthSession(retries=5)
```

### 4. Fetching Data with Custom Headers
```python
sr.fetch_cookies("https://www.example.com")
custom_headers = {"User-Agent": "Custom-UA"}
sr.set_headers(custom_headers)
response = sr.get("https://www.example.com/api")
print(response.text)
```

### 5. Handling Different HTTP Methods
```python
sr.post("https://www.example.com/api", json={"key": "value"})
sr.put("https://www.example.com/api", json={"key": "updated_value"})
sr.delete("https://www.example.com/api")
```

### 6. Clearing Cookies
```python
sr.clear_cookies()
```

### 7. Retry using Tenacity (nightly)
```python
from tenacity import retry

@retry
def get_response(url):
    sr = StealthSession()
    response = sr.get(url)
    return response.json()

get_response("https://www.example.com/api")
```



## License
This project is licensed under the MIT License.

