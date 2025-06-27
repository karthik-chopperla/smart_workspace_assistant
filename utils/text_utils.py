import re
import string

def clean_text(text):
    """
    Cleans and normalizes text: lowercases, removes punctuation, trims spaces.
    Accepts str, list, or None.
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
    Splits text into sentences using punctuation as delimiters.
    """
    if not isinstance(text, str):
        text = clean_text(text)
    sentences = re.split(r'[.!?]', text)
    return [s.strip() for s in sentences if s.strip()]


def tokenize_words(text):
    """
    Splits cleaned text into individual words.
    """
    cleaned = clean_text(text)
    return cleaned.split()


def compute_word_freq(words):
    """
    Builds a frequency dictionary for a list of words.
    """
    if not isinstance(words, list):
        words = tokenize_words(words)

    freq = {}
    for word in words:
        if word:
            freq[word] = freq.get(word, 0) + 1
    return freq
