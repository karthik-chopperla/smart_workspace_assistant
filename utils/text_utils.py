import re
import string

def clean_text(text):
    """
    Safely clean input text:
    - Accepts strings, lists, None, or any other type
    - Returns lowercase, punctuation-free, stripped text
    """
    if not isinstance(text, str):
        if isinstance(text, list):
            text = " ".join(map(str, text))
        elif text is None:
            text = ""
        else:
            text = str(text)

    text = text.lower()
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def tokenize_sentences(text):
    """
    Split text into individual sentences.
    """
    if not isinstance(text, str):
        text = clean_text(text)

    sentences = re.split(r'[.!?]', text)
    return [s.strip() for s in sentences if s.strip()]


def tokenize_words(text):
    """
    Tokenize text into individual words.
    """
    cleaned = clean_text(text)
    return cleaned.split() if isinstance(cleaned, str) else []


def compute_word_freq(words):
    """
    Compute word frequency from a list or string.
    """
    if not isinstance(words, list):
        words = tokenize_words(words)

    freq = {}
    for word in words:
        word = str(word).strip().lower()
        if word:
            freq[word] = freq.get(word, 0) + 1
    return freq
