from scanner.findings import HEADER_FINDINGS


def build_findings(header_results):

    findings = []

    for header, present in header_results.items():

        if not present and header in HEADER_FINDINGS:

            finding_info = HEADER_FINDINGS[header]

            findings.append(
                {
                    "title": f"Missing {header}",
                    "severity": finding_info["severity"],
                    "owasp": finding_info["owasp"],
                    "description": finding_info["description"],
                    "recommendation": finding_info["recommendation"]
                }
            )

    return findings