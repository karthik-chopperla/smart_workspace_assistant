import streamlit as st
from modules.feedback_loop import update_logic_based_on_feedback
from utils.storage import save_feedback, load_feedback_history


def feedback_ui():
    st.header("🧪 Feedback Center")
    st.markdown(
        """
        Help improve the assistant by rating:
        - Summary accuracy
        - Task relevance
        - Schedule usefulness
        - Note grouping logic
        """
    )

    rating_summary = st.slider("📌 Summary Quality (0 - Poor, 5 - Excellent)", 0, 5, 3)
    rating_tasks = st.slider("🗂️ Task Extraction Accuracy", 0, 5, 3)
    rating_schedule = st.slider("📅 Schedule Usefulness", 0, 5, 3)
    rating_notes = st.slider("🗒️ Note Organization Quality", 0, 5, 3)

    if st.button("📤 Submit Feedback"):
        feedback = {
            "summary": rating_summary,
            "tasks": rating_tasks,
            "schedule": rating_schedule,
            "notes": rating_notes
        }

        # Save & update learning loop
        save_feedback(feedback)
        update_logic_based_on_feedback(feedback)

        st.success("Feedback Submitted ✅")

    st.markdown("---")
    st.subheader("🧾 Previous Feedback Ratings")
    hist = load_feedback_history()
    if hist:
        for i, f in enumerate(hist[::-1]):
            st.markdown(f"**Feedback #{len(hist)-i}** — Summary: {f['summary']}, Tasks: {f['tasks']}, Schedule: {f['schedule']}, Notes: {f['notes']}")
    else:
        st.caption("No feedback submitted yet.")
