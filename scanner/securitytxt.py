import requests


def check_security_txt(url):

    try:

        clean_url = (
            url.replace("https://", "")
               .replace("http://", "")
               .strip("/")
        )

        target = (
            f"https://{clean_url}/.well-known/security.txt"
        )

        response = requests.get(
            target,
            timeout=5,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        return {
            "found": response.status_code == 200,
            "url": target,
            "status_code": response.status_code
        }

    except Exception:

        return {
            "found": False,
            "url": None,
            "status_code": None
        }