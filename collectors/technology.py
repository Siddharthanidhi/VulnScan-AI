from collectors.base import BaseCollector
from collectors.registry import register

from analyzers.fingerprint import detect


@register
class TechnologyCollector(BaseCollector):

    id = "technology"

    name = "Technology Fingerprinting"

    def collect(self, context):

        if context.response is None:

            context.collector_results[self.id] = {
                "success": False
            }

            return

        technologies = detect(
            context.response.headers
        )

        context.collector_results[self.id] = {

            "success": True,

            "technologies": technologies

        }