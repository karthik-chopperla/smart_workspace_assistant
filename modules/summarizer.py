# summarizer.py
from utils.text_utils import (
    clean_text,
    tokenize_sentences,
    tokenize_words,
    compute_word_freq,
    extract_tasks
)

def summarize_email(email_text):
    if not isinstance(email_text, str):
        return {
            "summary": "",
            "tasks": []
        }

    sentences = tokenize_sentences(email_text)
    words = tokenize_words(email_text)
    freq = compute_word_freq(words)

    # Score sentences based on word frequency
    sentence_scores = {}
    for sentence in sentences:
        word_list = tokenize_words(sentence)
        sentence_scores[sentence] = sum(freq.get(word, 0) for word in word_list)

    # Select top 3 sentences
    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:3]
    summary = " ".join(top_sentences).strip()

    # Extract actionable tasks
    tasks = extract_tasks(email_text)

    return {
        "summary": summary,
        "tasks": tasks
    }
