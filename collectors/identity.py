import socket
from urllib.parse import urlparse

from collectors.base import BaseCollector
from collectors.registry import register


@register
class IdentityCollector(BaseCollector):

    id = "identity"

    name = "Target Identity"

    def collect(self, context):

        target = context.target

        if not target.startswith(("http://", "https://")):
            target = "https://" + target

        hostname = urlparse(target).hostname

        try:

            ip = socket.gethostbyname(hostname)

        except Exception:

            ip = None

        context.collector_results[self.id] = {

            "success": True,

            "hostname": hostname,

            "ip": ip

        }