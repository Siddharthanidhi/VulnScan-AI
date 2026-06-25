from datetime import datetime
from scanner.identity import get_identity


def build_evidence_package(
    target,
    certificate,
    header_data,
    cookies,
    security_txt,
    robots_txt,
    technologies,
):

    secure = 0
    insecure = 0

    for cookie in cookies:
        if cookie["secure"]:
            secure += 1
        else:
            insecure += 1

    identity = get_identity(target, header_data)

    evidence = {
        "scan_information": {

            "timestamp": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        },

        "identity": identity,
        
        "certificate": certificate,
        "headers": {
            "observed": header_data["headers"],
            "raw": header_data["raw_headers"],
            "status_code": header_data["status_code"],
            "final_url": header_data["final_url"],
        },
        "cookies": {
            "total": len(cookies),
            "secure": secure,
            "insecure": insecure,
            "details": cookies,
        },
        "security_files": {"security_txt": security_txt, "robots_txt": robots_txt},
        "technology": {"detected": technologies},
        "limitations": [],
    }

    # ---------- Automatic limitations ----------

    raw = {k.lower(): v for k, v in header_data["raw_headers"].items()}

    if "x-amzn-waf-action" in raw:
        evidence["limitations"].append(
            "AWS WAF challenge detected. Automated responses may differ from browser responses."
        )

    return evidence
