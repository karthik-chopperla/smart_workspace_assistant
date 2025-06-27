from utils.text_utils import tokenize_sentences, tokenize_words, clean_text

def extract_tasks(email_text: str) -> list:
    """
    Simulated AI-style task extractor.
    Identifies sentences that include actionable task-like keywords.
    """

    if not isinstance(email_text, str):
        email_text = str(email_text or "")

    tasks = []
    action_keywords = [
        "finalize", "send", "schedule", "prepare", "compile",
        "check", "label", "meet", "submit", "report", "call", "organize", "review"
    ]

    for sentence in tokenize_sentences(email_text):
        sentence_lower = sentence.lower()
        if any(kw in sentence_lower for kw in action_keywords):
            tasks.append(sentence.strip())

    return tasks
