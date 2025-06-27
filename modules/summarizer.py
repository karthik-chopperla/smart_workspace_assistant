import re
import math
from utils.text_utils import clean_text, tokenize_sentences, tokenize_words, compute_word_freq


def summarize_email(email_text: str, max_sentences: int = 3) -> str:
    """
    Summarizes an email using frequency-based sentence scoring.
    No pretrained model or API is used — logic is generated dynamically.
    """
    if not email_text.strip():
        return "No content provided."

    # Step 1: Preprocess and clean
    cleaned_text = clean_text(email_text)

    # Step 2: Tokenize
    sentences = tokenize_sentences(cleaned_text)
    words = tokenize_words(cleaned_text)
    if not sentences or not words:
        return "Not enough content to summarize."

    # Step 3: Compute word frequencies
    freq = compute_word_freq(words)

    # Step 4: Score each sentence based on word frequencies
    sentence_scores = {}
    for sent in sentences:
        sent_words = tokenize_words(sent)
        sent_score = sum(freq.get(word, 0) for word in sent_words)
        sentence_scores[sent] = sent_score / len(sent_words) if sent_words else 0

    # Step 5: Select top-ranked sentences
    ranked_sentences = sorted(sentence_scores.items(), key=lambda item: item[1], reverse=True)
    selected_sentences = [s[0] for s in ranked_sentences[:max_sentences]]

    # Step 6: Return ordered summary (preserving input order)
    summary = [s for s in sentences if s in selected_sentences]
    return " ".join(summary)
