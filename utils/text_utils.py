import re
import string

def clean_text(text):
    """
    Clean and normalize input text.
    Handles strings, None, lists, or other data types gracefully.
    """
    if not isinstance(text, str):
        if isinstance(text, list):
            text = " ".join(map(str, text))
        elif text is None:
            text = ""
        else:
            text = str(text)

    # Lowercase
    text = text.lower()
    # Remove punctuation
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def tokenize_sentences(text):
    """
    Split cleaned text into a list of sentences.
    """
    if not isinstance(text, str):
        text = clean_text(text)
    sentences = re.split(r'[.!?]', text)
    return [s.strip() for s in sentences if s.strip()]


def tokenize_words(text):
    """
    Tokenize cleaned text into a list of words.
    """
    cleaned = clean_text(text)
    return cleaned.split() if isinstance(cleaned, str) else []


def compute_word_freq(words):
    """
    Calculate frequency of each word from a list or raw text.
    """
    if not isinstance(words, list):
        words = tokenize_words(words)

    freq = {}
    for word in words:
        word = word.strip().lower()
        if word:
            freq[word] = freq.get(word, 0) + 1
    return freq
