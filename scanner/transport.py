import requests


def analyze_transport(url):

    try:

        clean_url = (
            url.replace("https://", "")
               .replace("http://", "")
               .strip("/")
        )

        http_url = f"http://{clean_url}"

        response = requests.get(
            http_url,
            allow_redirects=True,
            timeout=10,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 "
                    "(Windows NT 10.0; Win64; x64)"
                )
            }
        )

        redirect_chain = []

        for redirect in response.history:

            redirect_chain.append(
                {
                    "status_code": redirect.status_code,
                    "url": redirect.url
                }
            )

        final_url = response.url

        https_enforced = (
            final_url.lower().startswith(
                "https://"
            )
        )

        return {
            "success": True,
            "initial_url": http_url,
            "final_url": final_url,
            "redirect_count": len(
                redirect_chain
            ),
            "redirect_chain": redirect_chain,
            "https_enforced": https_enforced
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }