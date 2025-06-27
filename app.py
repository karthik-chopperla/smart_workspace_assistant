import streamlit as st

# Import UI components
from ui.email_ui import email_ui
from ui.schedule_ui import schedule_ui
from ui.notes_ui import notes_ui
from ui.feedback_ui import feedback_ui

# Configure Streamlit App Settings
st.set_page_config(
    page_title="Smart Workspace Assistant",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and Introduction
st.title("🧠 Smart Workspace Assistant")
st.markdown(
    """
    A fully AI-generated productivity assistant that helps you:
    - ✉️ Summarize emails and extract tasks
    - 📅 Build smart daily schedules
    - 🗒️ Organize and cluster notes
    - 🧪 Learn and improve based on your feedback
    
    ✅ Built entirely by AI | ☁️ Deployable on Streamlit Cloud | 💻 Runs on CPU
    """
)

# Sidebar Navigation
st.sidebar.title("🔧 Assistant Modules")
selection = st.sidebar.radio(
    "Choose a module",
    ["📧 Email Summarizer", "📅 Smart Scheduler", "🗒️ Note Manager", "🧪 Feedback"],
    index=0
)

# Dynamic Routing
if selection == "📧 Email Summarizer":
    email_ui()
elif selection == "📅 Smart Scheduler":
    schedule_ui()
elif selection == "🗒️ Note Manager":
    notes_ui()
elif selection == "🧪 Feedback":
    feedback_ui()

# Footer
#st.markdown("---")
#st.caption("⚙️ Built 100% using AI — no APIs, no hardcoded logic, no manual coding.")
#st.caption("🔗 Open-source | 🔬 AI-driven logic | 🚀 Deploy with Streamlit.app")
