from collectors.base import BaseCollector
from collectors.registry import register

from scanner.certificate import get_certificate_info


@register
class CertificateCollector(BaseCollector):

    id = "certificate"

    name = "TLS Certificate"

    def collect(self, context):

        result = get_certificate_info(
            context.target
        )

        context.collector_results[
            self.id
        ] = result