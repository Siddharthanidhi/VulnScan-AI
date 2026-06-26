HEADER_EXPLANATIONS = {
    "Content-Security-Policy":
        "Helps reduce the impact of cross-site scripting attacks.",

    "Strict-Transport-Security":
        "Forces browsers to communicate over HTTPS.",

    "X-Frame-Options":
        "Helps protect against clickjacking attacks.",

    "X-Content-Type-Options":
        "Prevents MIME-type sniffing by browsers.",

    "Referrer-Policy":
        "Controls how much referrer information is shared."
}


def build_observations(evidence_package):

    observations = []

    collectors = evidence_package["collectors"]

    # =============================
    # Security Headers
    # =============================

    headers = collectors["headers"]["headers"]

    raw_headers = {
        k.lower(): v
        for k, v in collectors["headers"]["raw_headers"].items()
    }

    for header, present in headers.items():

        header_key = header.lower()

        evidence = []

        if header_key in raw_headers:

            evidence.append(
                f"{header}: {raw_headers[header_key]}"
            )

        observations.append({

            "category": "Security Headers",

            "title": header,

            "status":
                "Observed"
                if present
                else "Not Observed",

            "confidence":
                "High"
                if present
                else "Medium",

            "evidence": evidence,

            "explanation":
                HEADER_EXPLANATIONS.get(
                    header,
                    ""
                )

        })

    # =============================
    # Certificate
    # =============================

    cert = collectors["certificate"]

    if cert["success"]:

        observations.append({

            "category": "Certificate",

            "title": "TLS Certificate",

            "status":
                "Valid"
                if not cert["expired"]
                else "Expired",

            "confidence": "High",

            "evidence": [

                f"Issuer: {cert['issuer']}",

                f"Valid Until: {cert['valid_until']}",

                f"Days Remaining: {cert['days_remaining']}"

            ],

            "explanation":
                "Certificate information collected from the TLS handshake."

        })

    # =============================
    # Technology Fingerprints
    # =============================

    for tech in collectors["technology"]["technologies"]:

        observations.append({

            "category": "Infrastructure",

            "title": tech["technology"],

            "status": "Detected",

            "confidence":
                f"{tech['confidence']}%",

            "evidence":
                tech["evidence"],

            "explanation":
                "Technology identified through HTTP response fingerprinting."

        })

    return observations