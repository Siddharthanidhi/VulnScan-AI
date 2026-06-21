import requests


def check_cookies(url):
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

        cookies = []

        for cookie in response.cookies:
            cookies.append(
                {
                    "name": cookie.name,
                    "secure": cookie.secure
                }
            )

        return cookies

    except Exception:
        return []