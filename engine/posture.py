from knowledge.rules import RULES


def build_posture(evidence):

    positives = []

    review_items = []

    for observation in evidence["observations"]:

        rule = RULES.get(observation["title"])

        if not rule:
            continue

        if observation["status"] in ("Observed", "Valid"):

            if rule["positive"]:

                positives.append(
                    rule["positive"]
                )

        elif observation["status"] == "Not Observed":

            if rule["review"]:

                review_items.append(
                    rule["review"]
                )

    score = evidence["risk"]["score"]

    if score >= 90:
        overall = "Excellent"

    elif score >= 75:
        overall = "Good"

    elif score >= 50:
        overall = "Moderate"

    else:
        overall = "Needs Review"

    summary = (
        f"This passive assessment identified "
        f"{len(positives)} positive security indicators "
        f"and {len(review_items)} items worth reviewing."
    )

    return {

        "overall": overall,

        "summary": summary,

        "positives": positives,

        "review_items": review_items,

        "confidence": "High"

    }