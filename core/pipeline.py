import requests

from core.context import ScanContext
from collectors.registry import COLLECTORS
import collectors.response
import collectors.headers

class ScanPipeline:

    def run(self, target):

        session = requests.Session()

        session.headers.update({

            "User-Agent":
            "VulnScanAI/1.0"

        })

        context = ScanContext(

            target=target,

            session=session

        )

        for collector in COLLECTORS:

            collector.collect(context)

        return context