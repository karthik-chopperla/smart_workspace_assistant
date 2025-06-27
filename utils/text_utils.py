import re

def clean_text(text):
    """Clean and lowercase the text."""
    if not isinstance(text, str):
        text = str(text) if text is not None else ""
    return text.strip().lower()

def tokenize_sentences(text):
    """Split cleaned text into individual sentences."""
    cleaned = clean_text(text)
    sentences = re.split(r'[.!?]', cleaned)
    return [s.strip() for s in sentences if s.strip()]

def tokenize_words(text):
    """Split cleaned text into individual words."""
    cleaned = clean_text(text)
    return cleaned.split()

def compute_word_freq(words):
    """Count word frequencies from a list of words."""
    freq = {}
    for word in words:
        if isinstance(word, str):
            freq[word] = freq.get(word, 0) + 1
    return freq

def extract_tasks(text):
    """Extract task-like sentences using task keywords."""
    task_keywords = [
        "finalize", "schedule", "prepare", "compile", "check",
        "make sure", "send", "submit", "review", "complete"
    ]
    sentences = tokenize_sentences(text)
    tasks = []

    for sentence in sentences:
        for keyword in task_keywords:
            if keyword in sentence.lower():
                tasks.append(sentence.strip())
                break
    return tasks
