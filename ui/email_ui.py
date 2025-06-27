import streamlit as st
from modules.summarizer import summarize_email

def email_ui():
    st.subheader("📧 Smart Email Summarizer")
    st.markdown(
        """
        Paste or type an email message below, and let the assistant:
        - Summarize it concisely
        - Extract actionable tasks and deadlines
        - Save your summary to your workspace
        """
    )

    user_email = st.text_area("✉️ Enter Email Text Here", height=300)

    if st.button("🔍 Summarize Email"):
        if user_email.strip():
            try:
                result = summarize_email(user_email)
                st.markdown("### 📝 Summary")
                st.success(result["summary"])

                st.markdown("### ✅ Actionable Tasks")
                if result["tasks"]:
                    for task in result["tasks"]:
                        st.write("- " + task)
                else:
                    st.info("No actionable tasks detected.")
            except Exception as e:
                st.error(f"An error occurred during summarization: {str(e)}")
        else:
            st.warning("Please enter some email content.")
