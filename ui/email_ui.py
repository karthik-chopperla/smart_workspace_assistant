import streamlit as st
from modules.summarizer import summarize_email

def email_ui():
    st.header("📧 Smart Email Summarizer")
    st.write("Paste or type an email message below, and let the assistant:")

    st.markdown("- Summarize it concisely")
    st.markdown("- Extract actionable tasks and deadlines")
    st.markdown("- Save your summary to your workspace")

    user_email = st.text_area("✉️ Enter Email Text Here", height=250)

    if st.button("Summarize Email"):
        if user_email.strip() == "":
            st.warning("Please enter an email to summarize.")
            return

        summary = summarize_email(user_email)

        st.success("✅ Email Summarized")

        st.subheader("📝 Summary")
        st.write(summary["summary"])

        st.subheader("📌 Extracted Tasks")
        if summary["tasks"]:
            for task in summary["tasks"]:
                st.markdown(f"- {task}")
        else:
            st.markdown("_No tasks found in the email._")
