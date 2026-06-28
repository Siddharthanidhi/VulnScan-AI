from knowledge.rules import RULES


def generate_recommendations(evidence_package):

    recommendations = []

    for observation in evidence_package["observations"]:

        title = observation["title"]
        status = observation["status"]

        rule = RULES.get(title)

        if not rule:
            continue

        if status in ("Not Observed", "Expired"):

            recommendations.append({

                "priority": "Medium",

                "title": title,

                "description": rule["recommendation"]

            })

        elif title == "TLS Certificate" and status == "Valid":

            recommendations.append({

                "priority": "Info",

                "title": "TLS Certificate",

                "description": rule["recommendation"]

            })

    return recommendations