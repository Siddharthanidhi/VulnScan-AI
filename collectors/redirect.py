from collectors.base import BaseCollector
from collectors.registry import register


@register
class RedirectCollector(BaseCollector):

    id = "redirect"

    name = "Redirect Analysis"

    def collect(self, context):

        if context.response is None:

            context.collector_results[self.id] = {
                "success": False
            }

            return

        response = context.response

        history = []

        for r in response.history:

            history.append({

                "status": r.status_code,

                "url": r.url

            })

        context.collector_results[self.id] = {

            "success": True,

            "redirect_count": len(history),

            "chain": history,

            "final_url": response.url,

            "https": response.url.startswith("https://")

        }