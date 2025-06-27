import re
import string

def clean_text(text):
    """
    Safely clean input text:
    - Converts any type (list, None, dict) to string
    - Lowercases, removes punctuation, trims whitespace
    """
    if not isinstance(text, str):
        if isinstance(text, list):
            text = " ".join([str(t) for t in text if t])
        else:
            text = str(text or "")
    
    text = text.lower()
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def tokenize_sentences(text):
    """
    Split input into sentences based on punctuation.
    """
    if not isinstance(text, str):
        text = clean_text(text)
    
    sentences = re.split(r'[.!?]', text)
    return [s.strip() for s in sentences if s.strip()]


def tokenize_words(text):
    """
    Tokenize text into words.
    """
    cleaned = clean_text(text)
    return cleaned.split() if isinstance(cleaned, str) else []


def compute_word_freq(words):
    """
    Compute frequency of each word from list or raw text.
    """
    freq = {}
    if not isinstance(words, list):
        words = tokenize_words(words)
    
    for word in words:
        word = str(word).strip().lower()
        if word:
            freq[word] = freq.get(word, 0) + 1
    return freq
