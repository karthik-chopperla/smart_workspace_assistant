import re

def clean_text(text):
    """Cleans and lowers the input text."""
    if not isinstance(text, str):
        raise TypeError(f"clean_text expected a string but got {type(text)}")
    return text.strip().lower()

def tokenize_sentences(text):
    """Split cleaned text into individual sentences."""
    cleaned = clean_text(text)
    sentences = re.split(r'[.!?]', cleaned)
    return [s.strip() for s in sentences if s.strip()]

def tokenize_words(text):
    """Split cleaned text into individual words."""
    if not isinstance(text, str):
        raise TypeError(f"tokenize_words expected a string but got {type(text)}")
    cleaned = clean_text(text)
    return cleaned.split()

def compute_word_freq(words):
    """Compute frequency of each word in a list."""
    if not isinstance(words, list):
        raise TypeError(f"compute_word_freq expected a list but got {type(words)}")
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
        for keyword in task_keywords:
            if keyword in sentence.lower():
                tasks.append(sentence.strip())
                break
    return tasks
