import requests

from core.context import ScanContext
from core.registry import COLLECTORS


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