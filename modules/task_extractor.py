from utils.text_utils import tokenize_sentences

def extract_tasks(email_text: str) -> list:
    """
    Extracts actionable tasks from email based on simple verb keywords.
    """

    if not isinstance(email_text, str):
        email_text = str(email_text or "")

    tasks = []
    action_keywords = [
        "finalize", "send", "schedule", "prepare", "compile", "check",
        "label", "meet", "submit", "report", "organize", "review", "update"
    ]

    for sentence in tokenize_sentences(email_text):
        if any(keyword in sentence.lower() for keyword in action_keywords):
            tasks.append(sentence.strip())

    return tasks
