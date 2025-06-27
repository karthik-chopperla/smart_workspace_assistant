import re
import string

def clean_text(text):
    """
    Cleans text by lowercasing, removing punctuation, and stripping whitespace.
    Handles None or invalid input safely.
    """
    if not isinstance(text, str):
        text = str(text or "")

    text = text.lower()
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def tokenize_sentences(text):
    """
    Splits text into sentences using period, newline, or question mark as delimiters.
    """
    if not isinstance(text, str):
        text = str(text or "")

    sentences = re.split(r'[.\n!?]+', text)
    return [s.strip() for s in sentences if s.strip()]


def tokenize_words(text):
    """
    Tokenizes text into words after cleaning it.
    """
    cleaned = clean_text(text)
    return cleaned.split()


def compute_word_freq(words):
    """
    Computes frequency of words in a list.
    """
    if not isinstance(words, list):
        words = [str(words)]

    freq = {}
    for word in words:
        if isinstance(word, str):
            freq[word] = freq.get(word, 0) + 1
    return freq
