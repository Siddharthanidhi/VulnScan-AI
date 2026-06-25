import socket
from urllib.parse import urlparse


def get_identity(target, header_data):

    final_url = header_data.get("final_url", target)

    parsed = urlparse(final_url)

    domain = parsed.netloc

    if not domain:
        domain = parsed.path

    ip_address = None

    try:
        ip_address = socket.gethostbyname(domain)

    except Exception:
        ip_address = "Unable to Resolve"

    return {

        "target": target,

        "final_url": final_url,

        "domain": domain,

        "ip_address": ip_address,

        "https": final_url.startswith("https://"),

        "status_code": header_data.get("status_code")

    }