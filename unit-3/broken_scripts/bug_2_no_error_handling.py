import requests

# BUG: Calling a URL that is down or times out without try-except handling
url = "https://httpbin.org/status/500"
response = requests.get(url, timeout=1)
response.raise_for_status()
print("Success!", response.status_code)
