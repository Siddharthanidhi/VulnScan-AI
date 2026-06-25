import requests

from collectors.base import BaseCollector
from collectors.registry import register


@register
class ResponseCollector(BaseCollector):

    id = "response"

    name = "HTTP Response"

    def collect(self, context):

        target = context.target

        if not target.startswith(("http://", "https://")):
            target = "https://" + target

        try:

            response = context.session.get(
                target,
                timeout=10,
                allow_redirects=True,
            )

            context.response = response

            context.collector_results[self.id] = {
                "success": True,
                "status_code": response.status_code,
                "final_url": response.url,
            }

        except Exception as e:

            context.collector_results[self.id] = {
                "success": False,
                "error": str(e),
            }