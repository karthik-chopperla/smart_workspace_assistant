from utils.text_utils import tokenize_sentences, tokenize_words, compute_word_freq
from modules.task_extractor import extract_tasks  # ✅ Make sure this import is correct

def summarize_email(email_text: str) -> dict:
    sentences = tokenize_sentences(email_text)
    words = tokenize_words(email_text)
    freq = compute_word_freq(words)

    sentence_scores = {}
    for sentence in sentences:
        if not isinstance(sentence, str):
            continue
        for word in tokenize_words(sentence):
            if word in freq:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + freq[word]

    top_sentences = [s for s in sorted(sentence_scores, key=sentence_scores.get, reverse=True) if isinstance(s, str)][:3]
    summary = " ".join(top_sentences).strip()
    tasks = extract_tasks(email_text)

    return {
        "summary": summary,
        "tasks": tasks
    }
