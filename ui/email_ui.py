import streamlit as st
from modules.summarizer import summarize_email
from utils.storage import save_to_session

def email_ui():
    st.subheader("📧 Smart Email Summarizer")
    st.markdown("""
    Paste or type an email message below, and let the assistant:
    - Summarize it concisely  
    - Extract actionable tasks and deadlines  
    - Save your summary to your workspace
    """)

    user_email = st.text_area("✉️ Enter Email Text Here", height=250)

    if st.button("🔍 Summarize Email"):
        if user_email.strip() == "":
            st.warning("Please enter an email message to summarize.")
            return

        summary_data = summarize_email(user_email)

        if summary_data:
            st.success("✅ Summary Generated")

            st.markdown("### ✨ Summary")
            st.write(summary_data["summary"])

            st.markdown("### 📌 Actionable Tasks")
            for task in summary_data["tasks"]:
                st.markdown(f"- [ ] {task}")

            save_to_session("email_summary", summary_data)
        else:
            st.error("❌ Unable to generate summary. Please check the input text.")
