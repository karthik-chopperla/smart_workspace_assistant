import streamlit as st
from modules.scheduler import generate_schedule
from utils.storage import load_task_history, save_schedule_data


def schedule_ui():
    st.header("📅 Smart Schedule Planner")
    st.markdown(
        """
        Based on tasks extracted from your emails, this assistant builds a smart schedule.

        - Prioritizes based on urgency, deadlines, and working hours.
        - You can adjust urgency to retrain schedule logic dynamically.
        """
    )

    # Load previously extracted tasks
    task_data = load_task_history()

    if not task_data:
        st.warning("No tasks found. Please summarize an email first.")
        return

    st.subheader("📝 Task List with Adjustable Urgency")
    task_inputs = []
    for idx, task in enumerate(task_data):
        urgency = st.slider(f"Urgency for: {task}", 1, 5, 3)
        task_inputs.append({"task": task, "urgency": urgency})

    if st.button("🧠 Generate Schedule"):
        schedule_blocks = generate_schedule(task_inputs)
        save_schedule_data(schedule_blocks)

        st.success("Schedule Generated ✅")
        st.subheader("📅 AI-Generated Schedule")

        for block in schedule_blocks:
            st.markdown(f"**{block['time_slot']}** → {block['task']}")

    st.markdown("---")
    st.subheader("📂 Previous Schedule (This Session)")
    prev = save_schedule_data(load_only=True)
    if prev:
        for block in prev:
            st.markdown(f"**{block['time_slot']}** → {block['task']}")
    else:
        st.caption("No schedule saved yet.")
