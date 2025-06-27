import re
from collections import Counter


def clean_text(text: str) -> str:
    """
    Lowercases, removes non-alphanumeric characters, and extra spaces.
    """
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def tokenize_sentences(text: str):
    """
    Splits text into individual sentences or note lines using:
    - Newlines
    - Periods followed by space
    """
    raw_sentences = re.split(r'[\n\r]+|(?<=[.])\s+', text)
    return [s.strip() for s in raw_sentences if s.strip()]


def tokenize_words(text: str):
    """
    Splits cleaned text into words.
    """
    cleaned = clean_text(text)
    return cleaned.split()


def compute_word_freq(text: str, top_n: int = 5):
    """
    Returns the top N most frequent words in the text.
    """
    words = tokenize_words(text)
    counter = Counter(words)
    return counter.most_common(top_n)
