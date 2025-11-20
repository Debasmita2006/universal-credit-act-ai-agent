import streamlit as st
from src.pdf_extractor import extract_text
from src.analyzer import analyze

st.set_page_config(page_title="Universal Credit Act 2025 – AI Agent", layout="wide")

st.title("📘 Universal Credit Act 2025 – AI Assistant")

st.write(
    "Upload the Universal Credit Act 2025 PDF and the agent will extract, "
    "summarise, and analyse it based on the assignment rules."
)

uploaded = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded is not None:
    text = extract_text(uploaded)

    st.subheader("📄 Extracted Text (Preview)")
    st.text(text[:2000] + ("\n...[truncated]..." if len(text) > 2000 else ""))

    result = analyze(text)

    st.subheader("🧠 Summary (Task 2)")
    for bullet in result["summary"]:
        st.markdown(f"- {bullet}")

    st.subheader("📂 Key Legislative Sections (Task 3)")
    st.markdown("**Definitions**")
    st.write(result["definitions"])
    st.markdown("**Obligations**")
    st.write(result["obligations"])
    st.markdown("**Responsibilities**")
    st.write(result["responsibilities"])
    st.markdown("**Eligibility**")
    st.write(result["eligibility"])
    st.markdown("**Payments / Entitlements**")
    st.write(result["payments"])
    st.markdown("**Penalties / Enforcement**")
    st.write(result["penalties"])
    st.markdown("**Record-keeping / Reporting**")
    st.write(result["record_keeping"])

    st.subheader("✅ Rule Checks (Task 4)")
    st.json(result["rules_check"])
