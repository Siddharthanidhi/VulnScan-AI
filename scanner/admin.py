import requests

COMMON_PATHS = [
    "/admin",
    "/administrator",
    "/login",
    "/dashboard",
    "/wp-admin",
]

KEYWORDS = [
    "login",
    "username",
    "password",
    "sign in",
    "dashboard",
    "admin"
]


def find_admin_pages(url):

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    findings = []

    for path in COMMON_PATHS:

        try:

            response = requests.get(
                url + path,
                timeout=5,
                allow_redirects=True,
                headers={
                    "User-Agent": "Mozilla/5.0"
                }
            )

            page_text = response.text.lower()

            keyword_found = any(
                keyword in page_text
                for keyword in KEYWORDS
            )

            same_path = path.strip("/") in response.url.lower()

            if (
                response.status_code == 200
                and keyword_found
                and same_path
            ):
                findings.append(path)

        except:
            pass

    return findings