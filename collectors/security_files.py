from collectors.base import BaseCollector
from collectors.registry import register

from scanner.securitytxt import check_security_txt
from scanner.robots import check_robots


@register
class SecurityFilesCollector(BaseCollector):

    id = "security_files"

    name = "Security Files"

    def collect(self, context):

        context.collector_results[self.id] = {

            "security_txt":
                check_security_txt(
                    context.target
                ),

            "robots_txt":
                check_robots(
                    context.target
                )
        }