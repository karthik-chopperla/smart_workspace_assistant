import streamlit as st
from modules.note_manager import organize_notes
from utils.storage import save_note, load_note_history


def notes_ui():
    st.markdown("## 🗒️ Intelligent Notes Manager")
    st.info("**Type your notes below. The assistant will:**\n\n"
            "- Organize them into groups or categories\n"
            "- Suggest smart titles\n"
            "- Save everything to your session workspace")

    note_text = st.text_area("### ✏️ Write your notes or paste text here", height=200)

    if st.button("🧠 Organize Notes"):
        if not note_text.strip():
            st.warning("Please enter some notes to organize.")
            return

        groups = organize_notes(note_text)
        save_note(note_text, groups)

        st.success("✅ Notes Organized")
        st.markdown("### 📌 Structured Notes")

        for group in groups:
            st.markdown(f"#### 📂 {group['topic']}")
            for item in group['items']:
                st.markdown(f"- {item}")
            st.markdown("---")

    if st.button("📁 View Note History"):
        note_history = load_note_history()
        if not note_history:
            st.info("No previous notes found.")
        else:
            st.markdown("### 🕘 Previous Notes")
            for idx, entry in enumerate(note_history[::-1], 1):
                st.markdown(f"#### 📄 Note #{idx}")
                st.markdown(f"**Original Input:**\n\n{entry['raw']}")
                st.markdown("**Organized Notes:**")
                for group in entry['groups']:
                    st.markdown(f"**📂 {group['topic']}**")
                    for item in group['items']:
                        st.markdown(f"- {item}")
                st.markdown("---")
