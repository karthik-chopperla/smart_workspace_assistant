import re
import string

def clean_text(text):
    """
    Safely cleans text by converting to lowercase, removing punctuation, and stripping extra spaces.
    Converts non-string input into string if needed.
    """
    if not isinstance(text, str):
        if isinstance(text, list):
            text = " ".join([str(t) for t in text])
        else:
            text = str(text or "")

    text = text.lower()
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def tokenize_sentences(text):
    """
    Splits text into sentences using basic punctuation.
    """
    if not isinstance(text, str):
        text = clean_text(text)

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
        words = tokenize_words(words)

    for word in words:
        if not isinstance(word, str):
            word = str(word)
        word = word.strip()
        if word:
            freq[word] = freq.get(word, 0) + 1

    return freq
