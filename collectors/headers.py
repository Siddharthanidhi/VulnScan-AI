from collectors.base import BaseCollector
from collectors.registry import register


SECURITY_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
]


@register
class HeaderCollector(BaseCollector):

    id = "headers"

    name = "HTTP Security Headers"

    def collect(self, context):

        if context.response is None:

            context.collector_results[self.id] = {
                "success": False,
                "error": "Response not available."
            }

            return

        response = context.response

        response_headers = {
            k.lower(): v
            for k, v in response.headers.items()
        }
        print(response_headers)

        found_headers = {}

        for header in SECURITY_HEADERS:
            found_headers[header] = (
                header.lower() in response_headers
            )

        context.collector_results[self.id] = {

            "success": True,

            "headers": found_headers,

            "raw_headers": dict(response.headers),

            "status_code": response.status_code,

            "final_url": response.url,
        }