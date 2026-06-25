def build_assessment(
    target,
    certificate,
    header_data,
    cookies,
    security_txt,
    robots_txt,
    technologies
):

    secure_cookies = 0
    insecure_cookies = 0

    for cookie in cookies:

        if cookie["secure"]:
            secure_cookies += 1

        else:
            insecure_cookies += 1

    return {

        "target": target,

        "certificate": {
            "valid": (
                certificate["success"]
                and not certificate["expired"]
            ),
            "issuer": certificate.get(
                "issuer"
            ),
            "days_remaining": certificate.get(
                "days_remaining"
            )
        },

        "security_files": {
            "security_txt": security_txt["found"],
            "robots_txt": robots_txt["found"]
        },

        "headers": header_data["headers"],

        "cookies": {
            "total": len(cookies),
            "secure": secure_cookies,
            "insecure": insecure_cookies
        },

        "technologies": technologies
    }