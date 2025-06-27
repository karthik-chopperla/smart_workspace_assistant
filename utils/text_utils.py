import re
from typing import List

def clean_text(text) -> str:
    """
    Cleans input text. Converts to string if it's a list or any non-string type.
    Removes special characters and lowercases it.
    """
    # Convert None or unsupported types to empty string
    if not isinstance(text, (str, list)):
        text = ""

    # If list, convert to string
    if isinstance(text, list):
        text = " ".join(str(x) for x in text)

    # Convert to lowercase and remove non-alphanumeric characters
    text = text.lower()
    text = ''.join(c for c in text if c.isalnum() or c.isspace())
    return text

def tokenize_sentences(text: str) -> List[str]:
    text = clean_text(text)
    return re.split(r'(?<=[.!?]) +', text)

def tokenize_words(text: str) -> List[str]:
    cleaned = clean_text(text)
    return cleaned.split()

def compute_word_freq(text: str) -> dict:
    words = tokenize_words(text)
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq
