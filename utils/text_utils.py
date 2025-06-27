import re

def clean_text(text):
    if not isinstance(text, str):
        text = str(text) if text is not None else ""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text.strip()

def tokenize_sentences(text):
    if not isinstance(text, str):
        text = str(text) if text is not None else ""
    sentences = re.split(r'[.!?]', text)
    return [s.strip() for s in sentences if s.strip()]

def tokenize_words(text):
    cleaned = clean_text(text)
    return cleaned.split()

def compute_word_freq(words):
    if not isinstance(words, list):
        return {}
    freq = {}
    for word in words:
        if isinstance(word, str):
            freq[word] = freq.get(word, 0) + 1
    return freq

def extract_tasks(text):
    if not isinstance(text, str):
        return []
    task_keywords = ["finalize", "schedule", "prepare", "compile", "check", "make sure"]
    sentences = tokenize_sentences(text)
    tasks = []
    for sentence in sentences:
        for keyword in task_keywords:
            if keyword in sentence.lower():
                tasks.append(sentence.strip())
                break
    return tasks
