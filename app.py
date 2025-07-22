import streamlit as st
from main import run_website_analysis

st.set_page_config(page_title="Website Analyzer Crew", layout="centered")
st.title(" Hyper-Powered Website Analyzer Crew ")
st.markdown("Analyze website content with LLM agents using **Hyperbrowser** and **crewAI**.")

url = st.text_input(
    "Enter the URL to analyze:",
    value="https://www.wired.com/story/how-to-fix-your-own-gadgets-and-why-you-should/"
)

if st.button("🔎 Analyze"):
    with st.spinner("Scraping and analyzing the content... please wait ⏳"):
        try:
            report = run_website_analysis(url)
            st.success("✅ Analysis complete! Report has been saved as a Markdown (.md) file.")
            st.markdown("### 📄 Final Report")
            st.markdown(report)
        except Exception as e:
            st.error(f"Something went wrong: {str(e)}")
