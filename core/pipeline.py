import requests

from core.context import ScanContext
from collectors.registry import COLLECTORS
from core.evidence import build_evidence_package
import collectors.response
import collectors.headers
import collectors.certificate
import collectors.cookies
import collectors.security_files
import collectors.technology
import collectors.methods
import collectors.redirect
import collectors.identity


class ScanPipeline:
    def run(self, target):

        session = requests.Session()

        session.headers.update({"User-Agent": "VulnScanAI/1.0"})

        context = ScanContext(target=target, session=session)

        for collector in COLLECTORS:
            collector.collect(context)

        context.evidence_package = build_evidence_package(
            context
        )

        return context

