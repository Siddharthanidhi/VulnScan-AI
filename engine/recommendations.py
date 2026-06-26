def generate_recommendations(evidence_package):

    recommendations = []

    observations = evidence_package["observations"]

    for observation in observations:

        title = observation["title"]
        status = observation["status"]

        if title == "Content-Security-Policy" and status == "Not Observed":

            recommendations.append({

                "priority": "High",

                "title": "Review Content Security Policy",

                "description":
                    "Consider implementing a Content-Security-Policy header to reduce the impact of script injection attacks."

            })

        elif title == "X-Frame-Options" and status == "Not Observed":

            recommendations.append({

                "priority": "Medium",

                "title": "Review Clickjacking Protection",

                "description":
                    "Consider enabling X-Frame-Options or CSP frame-ancestors if appropriate."

            })

        elif title == "X-Content-Type-Options" and status == "Not Observed":

            recommendations.append({

                "priority": "Medium",

                "title": "Prevent MIME Sniffing",

                "description":
                    "Consider enabling X-Content-Type-Options: nosniff."

            })

        elif title == "Referrer-Policy" and status == "Not Observed":

            recommendations.append({

                "priority": "Low",

                "title": "Review Referrer Policy",

                "description":
                    "Review whether a Referrer-Policy header should be configured."

            })

        elif title == "TLS Certificate" and status == "Valid":

            recommendations.append({

                "priority": "Info",

                "title": "TLS Certificate",

                "description":
                    "TLS certificate is valid. Continue monitoring before expiration."

            })

    return recommendations