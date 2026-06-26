FINGERPRINTS = {
    "Amazon CloudFront": {
        "headers": [
            "x-amz-cf-id",
            "x-cache",
            "via"
        ]
    },

    "AWS WAF": {
        "headers": [
            "x-amzn-waf-action"
        ]
    },

    "Cloudflare": {
        "headers": [
            "cf-ray",
            "cf-cache-status"
        ]
    },

    "Nginx": {
        "server_contains": "nginx"
    },

    "Apache": {
        "server_contains": "apache"
    },

    "Microsoft IIS": {
        "server_contains": "iis"
    }
}


def detect(headers):

    headers = {
        k.lower(): v
        for k, v in headers.items()
    }

    detected = []

    server = headers.get("server", "").lower()

    for technology, fingerprint in FINGERPRINTS.items():

        matched = []
        expected = 0

        if "headers" in fingerprint:

            expected += len(
                fingerprint["headers"]
            )

            for header in fingerprint["headers"]:

                if header in headers:
                    matched.append(header)

        if "server_contains" in fingerprint:

            expected += 1

            if fingerprint["server_contains"] in server:
                matched.append("server")

        if matched:

            confidence = round(
                len(matched) / expected * 100
            )

            detected.append({

                "technology": technology,

                "confidence": confidence,

                "matched": len(matched),

                "expected": expected,

                "evidence": matched

            })

    return detected