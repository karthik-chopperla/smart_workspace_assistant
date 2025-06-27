import streamlit as st
from modules.summarizer import summarize_email
from modules.task_extractor import extract_tasks_from_summary
from utils.storage import save_email_data, load_email_history


def email_ui():
    st.header("📧 Smart Email Summarizer")
    st.markdown(
        """
        Paste or type an email message below, and let the assistant:
        - Summarize it concisely
        - Extract actionable tasks and deadlines
        - Save your summary to your workspace
        """
    )

    # Input Email
    user_email = st.text_area("✉️ Enter Email Text Here", height=200)

    # Submit Button
    if st.button("🧠 Summarize and Extract"):
        if user_email.strip():
            # Run AI summarizer
            summary = summarize_email(user_email)

            # Extract tasks from summary
            tasks = extract_tasks_from_summary(summary)

            # Save email + summary to session/history
            save_email_data(user_email, summary, tasks)

            # Display Results
            st.success("Summary Generated ✅")
            st.subheader("📌 Summary")
            st.write(summary)

            st.subheader("🗂️ Extracted Tasks")
            if tasks:
                for i, task in enumerate(tasks, 1):
                    st.markdown(f"**{i}.** {task}")
            else:
                st.info("No clear tasks or deadlines were identified.")

        else:
            st.warning("Please enter an email first.")

    # Display history of email interactions
    st.markdown("---")
    st.subheader("📚 Previous Emails (This Session)")
    email_history = load_email_history()
    if email_history:
        for idx, entry in enumerate(email_history[::-1]):
            with st.expander(f"Email #{len(email_history) - idx} Summary"):
                st.markdown("**Original Email:**")
                st.text(entry["email"])
                st.markdown("**Summary:**")
                st.write(entry["summary"])
                st.markdown("**Tasks:**")
                for t in entry["tasks"]:
                    st.markdown(f"- {t}")
    else:
        st.caption("No emails processed yet.")
