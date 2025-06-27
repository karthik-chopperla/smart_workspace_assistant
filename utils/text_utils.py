import re
from typing import List

def clean_text(text: str) -> str:
    """
    Cleans the input text: removes special characters, lowercases everything.
    If a list is accidentally passed, it's converted to a single string first.
    """
    if isinstance(text, list):
        text = " ".join(text)

    text = text.lower()
    text = ''.join(c for c in text if c.isalnum() or c.isspace())
    return text

def tokenize_sentences(text: str) -> List[str]:
    """
    Splits the text into sentences based on punctuation.
    """
    text = clean_text(text)
    return re.split(r'(?<=[.!?]) +', text)

def tokenize_words(text: str) -> List[str]:
    """
    Tokenizes a string into words using spaces. Cleans the text first.
    """
    cleaned = clean_text(text)
    return cleaned.split()

def compute_word_freq(text: str) -> dict:
    """
    Computes the frequency of each word in the text.
    """
    words = tokenize_words(text)
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq
