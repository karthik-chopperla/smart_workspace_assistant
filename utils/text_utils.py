import re
from typing import List, Union

def clean_text(text: Union[str, List, None]) -> str:
    """
    Cleans input text by removing special characters and converting to lowercase.
    Handles None, lists, or non-string inputs safely.
    """
    if text is None:
        return ""
    if isinstance(text, list):
        text = " ".join(str(x) for x in text)
    if not isinstance(text, str):
        text = str(text)

    text = text.lower()
    text = ''.join(c for c in text if c.isalnum() or c.isspace())
    return text

def tokenize_sentences(text: str) -> List[str]:
    cleaned = clean_text(text)
    return re.split(r'(?<=[.!?]) +', cleaned)

def tokenize_words(text: str) -> List[str]:
    cleaned = clean_text(text)
    return cleaned.split()

def compute_word_freq(words: Union[str, List[str]]) -> dict:
    """
    Computes frequency of words from a string or list of words.
    """
    if isinstance(words, str):
        words = tokenize_words(words)
    if not isinstance(words, list):
        return {}

    freq = {}
    for word in words:
        if isinstance(word, str):
            word = word.lower()
            freq[word] = freq.get(word, 0) + 1
    return freq
