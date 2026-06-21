import streamlit as st
from scanner.analyzer import build_findings
from scanner.headers import check_headers
from scanner.cookies import check_cookies
from scanner.admin import find_admin_pages
from scanner.scoring import calculate_score, get_risk_level

st.set_page_config(
    page_title="Website Vulnerability Scanner",
    layout="wide"
)

st.title("🛡️ Website Vulnerability Scanner")

st.write(
    "Analyze websites for common security misconfigurations."
)

url = st.text_input(
    "Website URL",
    placeholder="https://example.com"
)

if st.button("Start Scan"):

    if not url:
        st.warning("Please enter a URL.")
        st.stop()

    with st.spinner("Scanning target..."):

        header_data = check_headers(url)

        if not header_data["success"]:
            st.error(header_data["error"])
            st.stop()

        cookies = check_cookies(url)

        admin_pages = find_admin_pages(url)

        findings = build_findings(
            header_data["headers"]
        )

        score = calculate_score(
            findings
        )

        risk = get_risk_level(score)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Security Score",
                score
            )

        with col2:
            st.metric(
                "Issues Found",
                len(findings)
            )

        with col3:
            st.metric(
                "Risk Level",
                risk
            )

    st.subheader("Risk Level")
    st.info(risk)

    st.subheader("Security Headers")
    for finding in findings:

        severity = finding["severity"]

        if severity == "High":
            st.error(
                f"🔴 {finding['title']}"
            )

        elif severity == "Medium":
            st.warning(
                f"🟡 {finding['title']}"
            )

        else:
            st.info(
                f"🔵 {finding['title']}"
            )

        with st.expander("View Details"):

            st.write(
                f"**OWASP:** {finding['owasp']}"
            )

            st.write(
                f"**Description:** {finding['description']}"
            )

            st.write(
                f"**Recommendation:** {finding['recommendation']}"
            )
    for header, present in header_data["headers"].items():

        if present:
            st.success(f"✅ {header} Present")

        else:
            st.error(f"❌ {header} Missing")

    st.subheader("Cookie Analysis")

    if cookies:

        for cookie in cookies:

            if cookie["secure"]:
                st.success(
                    f"{cookie['name']} - Secure"
                )

            else:
                st.warning(
                    f"{cookie['name']} - Not Secure"
                )

    else:
        st.info("No cookies detected.")

    st.subheader("Administrative Endpoints")

    if admin_pages:

        for page in admin_pages:
            st.warning(page)

    else:
        st.success(
            "No common admin pages detected."
        )

    st.subheader("Recommendations")

    recommendations = []

    for header, present in header_data["headers"].items():

        if not present:
            recommendations.append(
                f"Enable {header}"
            )

    if admin_pages:
        recommendations.append(
            "Restrict access to administrative endpoints."
        )

    if recommendations:

        for rec in recommendations:
            st.write("•", rec)

    else:
        st.success(
            "No major issues detected."
        )