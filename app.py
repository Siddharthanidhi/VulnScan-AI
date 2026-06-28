import streamlit as st

from core.pipeline import ScanPipeline


st.set_page_config(page_title="VulnScan AI", page_icon="🛡️", layout="wide")

st.title("🛡️ VulnScan AI")
st.caption("Passive Website Security Assessment Platform")

st.write(
    """
Analyze a website using passive reconnaissance techniques.

This assessment does **not** perform penetration testing or exploit vulnerabilities.
It collects observable security evidence and generates an evidence-based assessment.
"""
)

url = st.text_input("Target Website", placeholder="https://example.com")

if st.button("Start Assessment", use_container_width=True):
    if not url:
        st.warning("Please enter a website URL.")

        st.stop()

    with st.spinner("Collecting security evidence..."):
        pipeline = ScanPipeline()

        context = pipeline.run(url)

        evidence = context.evidence_package

    risk = evidence["risk"]

    # ============================================================
    # Dashboard
    # ============================================================

    st.subheader("📊 Assessment Overview")

    col1, col2, col3 = st.columns(3)

    posture = evidence["posture"]

    col1, col2 = st.columns([1, 2])

    with col1:
        st.metric("Security Score", f"{risk['score']}/100")

        st.metric("Overall Posture", posture["overall"])

    with col2:
        st.info(posture["summary"])

        st.markdown("### ✅ Positive Signals")

        if posture["positives"]:
            for item in posture["positives"]:
                st.success(item)

        else:
            st.info("No positive signals identified.")

        st.markdown("### 🔎 Items Worth Reviewing")

        if posture["review_items"]:
            for item in posture["review_items"]:
                st.warning(item)

        else:
            st.success("Nothing noteworthy to review.")

        st.caption(f"Assessment Confidence: {posture['confidence']}")

    st.divider()

    # ============================================================
    # Observations
    # ============================================================

    st.subheader("🧠 Security Assessment")

    for item in evidence["interpretations"]:
        with st.container(border=True):
            st.markdown(f"### {item['title']}")

            st.markdown("**🔍 What we observed**")
            st.write(item["observation"])

            st.markdown("**📖 Why it matters**")
            st.write(item["importance"])

            st.markdown("**⚖️ What this means**")
            st.write(item["impact"])

            st.markdown("**✅ Recommended action**")
            st.write(item["action"])

            st.divider()

    # ============================================================
    # Recommendations
    # ============================================================

    st.subheader("💡 Recommendations")

    for recommendation in evidence["recommendations"]:
        st.info(
            f"**{recommendation['priority']} Priority**\n\n"
            f"**{recommendation['title']}**\n\n"
            f"{recommendation['description']}"
        )

    st.divider()

    # ============================================================
    # Assessment Limitations
    # ============================================================

    st.subheader("⚠️ Assessment Limitations")

    for limitation in evidence["limitations"]:
        st.warning(limitation)

    st.divider()

    # ============================================================
    # Collector Results
    # ============================================================

    st.subheader("📦 Collector Results")

    collectors = evidence["collectors"]

    for name, result in collectors.items():
        with st.expander(name.replace("_", " ").title()):
            st.json(result)

    st.divider()

    # ============================================================
    # Full Evidence Package
    # ============================================================

    st.subheader("🧠 Evidence Package")

    with st.expander("View Complete Evidence Package"):
        st.json(evidence)
