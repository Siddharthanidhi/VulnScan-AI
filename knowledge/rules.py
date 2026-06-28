RULES = {

    "Content-Security-Policy": {

        "importance":
            "Content Security Policy helps reduce the impact of cross-site scripting attacks.",

        "impact":
            "Its absence alone does not confirm a vulnerability, but reviewing the policy is considered good practice.",

        "recommendation":
            "Review whether a Content-Security-Policy is intentionally configured.",

        "positive":
            None,

        "review":
            "Content-Security-Policy was not observed.",

        "weight":
            -10

    },

    "Strict-Transport-Security": {

        "importance":
            "HSTS instructs browsers to always use HTTPS.",

        "impact":
            "When present it helps protect against protocol downgrade attacks.",

        "recommendation":
            "No action required if HTTPS is consistently enforced.",

        "positive":
            "HTTPS enforcement (HSTS) was observed.",

        "review":
            None,

        "weight":
            5

    },

    "X-Frame-Options": {

        "importance":
            "Helps protect against clickjacking attacks.",

        "impact":
            "Its absence may increase exposure to clickjacking in some applications.",

        "recommendation":
            "Review clickjacking protection using X-Frame-Options or frame-ancestors.",

        "positive":
            None,

        "review":
            "X-Frame-Options was not observed.",

        "weight":
            -5

    },

    "X-Content-Type-Options": {

        "importance":
            "Prevents MIME-type sniffing by browsers.",

        "impact":
            "Its absence may allow browsers to interpret content differently than intended.",

        "recommendation":
            "Consider enabling X-Content-Type-Options: nosniff.",

        "positive":
            None,

        "review":
            "X-Content-Type-Options was not observed.",

        "weight":
            -5

    },

    "Referrer-Policy": {

        "importance":
            "Controls how much referrer information is shared.",

        "impact":
            "A suitable policy can reduce unnecessary information disclosure.",

        "recommendation":
            "Review whether a Referrer-Policy should be configured.",

        "positive":
            None,

        "review":
            "Referrer-Policy was not observed.",

        "weight":
            -3

    },

    "TLS Certificate": {

        "importance":
            "TLS encrypts communication between users and the website.",

        "impact":
            "A valid certificate indicates encrypted communication is available.",

        "recommendation":
            "Continue monitoring certificate expiration.",

        "positive":
            "A valid TLS certificate was observed.",

        "review":
            None,

        "weight":
            5

    }

}