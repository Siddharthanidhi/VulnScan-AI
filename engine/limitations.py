def generate_limitations(evidence_package):

    limitations = [

        "This assessment is based on passive analysis only.",

        "No authenticated areas of the application were tested.",

        "No active exploitation or penetration testing was performed.",

        "No JavaScript execution or browser automation was used.",

        "The assessment is limited to the observed HTTP responses.",

        "Some security controls may not be observable through passive inspection alone."

    ]

    collectors = evidence_package["collectors"]

    if collectors["methods"]["allow_header_present"] is False:

        limitations.append(

            "Supported HTTP methods could not be fully determined because the Allow header was not present."

        )

    return limitations