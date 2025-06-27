import streamlit as st
from modules.summarizer import summarize_email

def email_ui():
    st.subheader("📧 Smart Email Summarizer")
    st.markdown("""
    Paste or type an email message below, and let the assistant:

    - Summarize it concisely  
    - Extract actionable tasks and deadlines  
    - Save your summary to your workspace  
    """)

    user_email = st.text_area("✉️ Enter Email Text Here", height=250)

    if st.button("Summarize Email"):
        if user_email.strip():
            result = summarize_email(user_email)
            st.success("✅ Email summarized!")

            st.markdown("### ✨ Summary")
            st.markdown(result["summary"])

            if result["tasks"]:
                st.markdown("### ✅ Actionable Tasks")
                for task in result["tasks"]:
                    st.markdown(f"- {task}")
            else:
                st.info("No actionable tasks found.")
        else:
            st.warning("Please enter an email to summarize.")
