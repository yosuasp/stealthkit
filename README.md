StealthKit
==========

StealthKit is a lightweight and customizable HTTP request engine designed to improve stealth and anti-bot evasion. It features dynamic user-agent rotation, proxy support, configurable headers, and optional cookie management to help developers make requests with minimal detection.

Features
--------

-   **Dynamic User-Agent Rotation** - Uses `fake_useragent` to generate realistic browser headers.
-   **Proxy Support** - Easily integrate a list of proxies for IP rotation.
-   **Customizable Headers** - Modify User-Agent and Referer dynamically.
-   **Cookie Management** - Enable or disable cookies based on your needs.
-   **Automatic Retries** - Retries failed requests to improve reliability.
-   **Session Persistence** - Maintains session-based browsing behavior when needed.

Installation
------------

```
pip install stealthkit

```

Basic Usage
-----------

```
from stealthkit import StealthRequests

stealth = StealthRequests(use_cookies=True, browsers=['Chrome', 'Firefox'], os=['Windows', 'Linux'])
response = stealth.get("https://example.com")
print(response.status_code)

```

Advanced Usage
--------------

### Custom Headers

```
stealth.set_headers(user_agent="Mozilla/5.0", referer="https://example.com")

```

### Using Proxies

```
stealth.set_proxies(["http://103.57.70.231:39143", "http://45.79.58.206:3128"])

```

### Custom Requests

```
response = stealth.request("POST", "https://example.com", data={"key": "value"})

```

Contributing
------------

Feel free to open issues or contribute to this repository by submitting a pull request!

License
-------

MIT License