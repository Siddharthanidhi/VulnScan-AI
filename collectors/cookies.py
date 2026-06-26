from collectors.base import BaseCollector
from collectors.registry import register

from scanner.cookies import check_cookies


@register
class CookieCollector(BaseCollector):

    id = "cookies"

    name = "Cookies"

    def collect(self, context):

        result = check_cookies(
            context.target
        )

        context.collector_results[
            self.id
        ] = result