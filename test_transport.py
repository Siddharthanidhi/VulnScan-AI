import requests

response = requests.get(
    "http://google.com",
    allow_redirects=False,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

print("STATUS:")
print(response.status_code)

print()

print("LOCATION:")
print(response.headers.get("Location"))

print()

print("HEADERS:")
for k, v in response.headers.items():
    print(f"{k}: {v}")