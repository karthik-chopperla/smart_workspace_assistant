import re

def clean_text(text):
    """
    Cleans input text: lowercases, removes special characters, strips extra spaces.
    Handles None and non-string types gracefully.
    """
    if not isinstance(text, str):
        text = str(text) if text is not None else ""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text.strip()

def tokenize_sentences(text):
    """
    Tokenize input text into a list of sentences.
    """
    if not isinstance(text, str):
        text = str(text) if text is not None else ""
    sentences = re.split(r'[.!?]', text)
    return [s.strip() for s in sentences if s.strip()]

def tokenize_words(text):
    """
    Tokenize text into individual words.
    """
    cleaned = clean_text(text)
    return cleaned.split()

def compute_word_freq(words):
    """
    Compute word frequency dictionary from list of words.
    """
    if not isinstance(words, list):
        return {}
    freq = {}
    for word in words:
        if isinstance(word, str):
            freq[word] = freq.get(word, 0) + 1
    return freq
