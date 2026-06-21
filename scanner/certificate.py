import socket
import ssl
from urllib.parse import urlparse
from datetime import datetime


def get_certificate_info(url):
    try:

        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        parsed = urlparse(url)

        hostname = parsed.netloc

        context = ssl.create_default_context()

        with socket.create_connection(
            (hostname, 443),
            timeout=10
        ) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=hostname
            ) as secure_sock:

                cert = secure_sock.getpeercert()

        issuer = dict(
            x[0]
            for x in cert["issuer"]
        )

        issued_to = dict(
            x[0]
            for x in cert["subject"]
        )

        valid_from = datetime.strptime(
            cert["notBefore"],
            "%b %d %H:%M:%S %Y %Z"
        )

        valid_until = datetime.strptime(
            cert["notAfter"],
            "%b %d %H:%M:%S %Y %Z"
        )

        days_remaining = (
            valid_until - datetime.utcnow()
        ).days

        return {
            "success": True,
            "hostname": hostname,
            "issuer": issuer.get("organizationName", "Unknown"),
            "issued_to": issued_to.get(
                "commonName",
                hostname
            ),
            "valid_from": valid_from.strftime(
                "%d %b %Y"
            ),
            "valid_until": valid_until.strftime(
                "%d %b %Y"
            ),
            "days_remaining": days_remaining,
            "expired": days_remaining < 0
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }