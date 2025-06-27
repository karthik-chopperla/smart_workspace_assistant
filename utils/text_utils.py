import re

def clean_text(text):
    """Cleans and lowers the input text."""
    if not isinstance(text, str):
        return ""
    return text.strip().lower()

def tokenize_sentences(text):
    """Split cleaned text into individual sentences."""
    if not isinstance(text, str):
        text = " ".join(text) if isinstance(text, list) else str(text)
    cleaned = clean_text(text)
    return [s.strip() for s in re.split(r'[.!?]', cleaned) if s.strip()]

def tokenize_words(text):
    """Split cleaned text into individual words."""
    if not isinstance(text, str):
        text = " ".join(text) if isinstance(text, list) else str(text)
    cleaned = clean_text(text)
    return cleaned.split()

def compute_word_freq(words):
    """Compute frequency of each word in a list."""
    freq = {}
    for word in words:
        if isinstance(word, str):
            freq[word] = freq.get(word, 0) + 1
    return freq

def extract_tasks(text):
    """Extract task-like sentences using task keywords."""
    task_keywords = ["finalize", "schedule", "prepare", "compile", "check", "make sure"]
    sentences = tokenize_sentences(text)
    tasks = []
    for sentence in sentences:
        if not isinstance(sentence, str):
            continue  # Skip non-strings
        for keyword in task_keywords:
            if keyword in sentence.lower():
                tasks.append(sentence.strip())
                break
    return tasks
