import streamlit as st


def save_email_data(email: str, summary: str, tasks: list):
    """
    Saves email, summary, and extracted tasks to session.
    """
    if "emails" not in st.session_state:
        st.session_state.emails = []

    st.session_state.emails.append({
        "email": email,
        "summary": summary,
        "tasks": tasks
    })


def load_email_history():
    return st.session_state.get("emails", [])


def load_task_history():
    """
    Aggregates tasks from past emails for scheduling.
    """
    emails = st.session_state.get("emails", [])
    all_tasks = []
    for e in emails:
        all_tasks.extend(e.get("tasks", []))
    return all_tasks


def save_schedule_data(schedule: list = None, load_only=False):
    """
    Saves or retrieves last generated schedule.
    Can be called with load_only=True to fetch data without passing schedule.
    """
    if load_only or schedule is None:
        return st.session_state.get("schedule", [])
    st.session_state.schedule = schedule


def save_note(raw_text: str, groups: list):
    """
    Saves raw note input and organized groups.
    """
    if "notes" not in st.session_state:
        st.session_state.notes = []
    st.session_state.notes.append({
        "raw": raw_text,
        "groups": groups
    })


def load_note_history():
    return st.session_state.get("notes", [])


def save_feedback(feedback: dict):
    """
    Saves user feedback ratings.
    """
    if "feedback" not in st.session_state:
        st.session_state.feedback = []
    st.session_state.feedback.append(feedback)


def load_feedback_history():
    return st.session_state.get("feedback", [])


def update_feedback_state(logic: dict):
    """
    Stores internal adjustments based on feedback. Simulated learning state.
    """
    st.session_state.feedback_logic = logic


def get_feedback_state():
    return st.session_state.get("feedback_logic", {})
