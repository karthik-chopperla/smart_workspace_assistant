import re
import string

def clean_text(text):
    """
    Safely cleans text by converting to lowercase, removing punctuation, and stripping extra spaces.
    Handles None, numbers, and other types gracefully.
    """
    if not isinstance(text, str):
        try:
            text = str(text or "")
        except:
            text = ""

    text = text.lower()
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def tokenize_sentences(text):
    """
    Splits text into sentences using basic punctuation.
    """
    if not isinstance(text, str):
        text = str(text or "")

    sentences = re.split(r'[.\n!?]+', text)
    return [s.strip() for s in sentences if s.strip()]


def tokenize_words(text):
    """
    Tokenizes cleaned text into words.
    """
    cleaned = clean_text(text)
    return cleaned.split()


def compute_word_freq(words):
    """
    Calculates word frequency from a list of words.
    """
    freq = {}
    if not isinstance(words, list):
        words = [str(words)]

    for word in words:
        if not isinstance(word, str):
            word = str(word)
        freq[word] = freq.get(word, 0) + 1

    return freq
