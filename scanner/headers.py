import requests

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy"
]


def check_headers(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        found_headers = {}

        response_headers = {
            k.lower(): v for k, v in response.headers.items()
        }

        for header in SECURITY_HEADERS:
            found_headers[header] = (
                header.lower() in response_headers
            )

        return {
            "success": True,
            "headers": found_headers,
            "status_code": response.status_code,
            "final_url": response.url
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }