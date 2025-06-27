import re

def clean_text(text):
    """Clean text by removing extra spaces and converting to lowercase."""
    if not isinstance(text, str):
        text = str(text) if text is not None else ""
    return text.strip().lower()

def tokenize_sentences(text):
    """Split text into sentences."""
    text = clean_text(text)
    sentences = re.split(r'[.!?]', text)
    return [s.strip() for s in sentences if s.strip()]

def tokenize_words(text):
    """Tokenize text into individual words."""
    text = clean_text(text)
    return re.findall(r'\b\w+\b', text)

def compute_word_freq(words):
    """Compute frequency of each word in a list of words."""
    if not isinstance(words, list):
        words = tokenize_words(words)
    freq = {}
    for word in words:
        if isinstance(word, str):
            freq[word] = freq.get(word, 0) + 1
    return freq

def extract_tasks(text):
    """Extract lines that seem to contain tasks based on action verbs."""
    task_keywords = ["finalize", "schedule", "prepare", "compile", "check", "make sure", "send", "review"]
    sentences = tokenize_sentences(text)
    tasks = []

    for sentence in sentences:
        for keyword in task_keywords:
            if keyword in sentence.lower():
                tasks.append(sentence.strip())
                break
    return tasks
