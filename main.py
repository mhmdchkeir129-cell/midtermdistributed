import requests

response = requests.get(
    "https://httpbin.org/get",
    timeout=10
)

print("Status:", response.status_code)
print("Python environment works!")