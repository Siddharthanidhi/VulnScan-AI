from knowledge.rules import RULES


def build_interpretations(evidence_package):

    interpretations = []

    for observation in evidence_package["observations"]:

        title = observation["title"]
        status = observation["status"]

        rule = RULES.get(title)

        if not rule:

            continue

        interpretation = {

            "title": title,

            "observation": "",

            "importance": rule["importance"],

            "impact": rule["impact"],

            "action": rule["recommendation"]

        }

        if status in ("Observed", "Valid", "Detected"):

            interpretation["observation"] = (
                f"{title} was observed during the assessment."
            )

        else:

            interpretation["observation"] = (
                f"{title} was not observed during the assessment."
            )

        interpretations.append(
            interpretation
        )

    return interpretations