from utils.text_utils import (
    clean_text,
    tokenize_sentences,
    tokenize_words,
    compute_word_freq,
    extract_tasks
)

def summarize_email(email_text, num_sentences=3):
    sentences = tokenize_sentences(email_text)
    words = tokenize_words(email_text)
    freq = compute_word_freq(words)

    sentence_scores = {}
    for sentence in sentences:
        score = 0
        for word in tokenize_words(sentence):
            score += freq.get(word, 0)
        sentence_scores[sentence] = score

    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    summary = " ".join(top_sentences).strip()
    tasks = extract_tasks(email_text)

    return {
        "summary": summary,
        "tasks": tasks
    }
