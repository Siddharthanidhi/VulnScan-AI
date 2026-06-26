from collectors.base import BaseCollector
from collectors.registry import register


@register
class HTTPMethodsCollector(BaseCollector):

    id = "methods"

    name = "HTTP Methods"

    def collect(self, context):

        if context.response is None:

            context.collector_results[self.id] = {
                "success": False
            }

            return

        response = context.response

        methods = []

        allow = response.headers.get("Allow")

        if allow:

            methods = [
                method.strip()
                for method in allow.split(",")
            ]

        context.collector_results[self.id] = {

            "success": True,

            "allowed_methods": methods,

            "allow_header_present": bool(allow)

        }