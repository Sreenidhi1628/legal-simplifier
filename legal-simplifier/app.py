import streamlit as st
from extractor import extract_text
from summarizer import summarize_text
from risk_detector import detect_risks
from translator import translate_to_tamil, translate_to_malayalam

st.title("Legal Document Simplifier")
st.subheader("Upload any Indian legal document and we will explain it simply!")
st.markdown("---")

uploaded_file = st.file_uploader("Upload your legal document (PDF)", type="pdf")
language = st.radio("Choose Output Language", ["English", "Tamil", "Malayalam"])

if uploaded_file is not None:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())
    with st.spinner("Reading your document..."):
        raw_text = extract_text("temp.pdf")
    st.success("Document read successfully!")
    with st.spinner("Simplifying the legal text..."):
        summary = summarize_text(raw_text)
        if language == "Tamil":
            with st.spinner("Translating to Tamil..."):
                summary = translate_to_tamil(summary)
        elif language == "Malayalam":
            with st.spinner("Translating to Malayalam..."):
                summary = translate_to_malayalam(summary)
    with st.spinner("Detecting risky clauses..."):
        risks = detect_risks(raw_text)
    st.markdown("---")
    st.header("Plain Language Summary")
    st.write(summary)
    st.markdown("---")
    st.header("Risky Clauses Found")
    if risks:
        for r in risks:
            clause = r["clause"]
            if language == "Tamil":
                clause = translate_to_tamil(clause)
            elif language == "Malayalam":
                clause = translate_to_malayalam(clause)
            st.warning(r["risk_word"].upper() + " -> " + clause)
    else:
        st.success("No major risk clauses found!")