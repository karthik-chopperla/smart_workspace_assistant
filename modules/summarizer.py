from utils.text_utils import tokenize_sentences, tokenize_words, compute_word_freq
from modules.task_extractor import extract_tasks

def summarize_email(email_text: str) -> dict:
    """
    Summarizes an email by extracting top sentences and tasks.
    Returns a dictionary with summary and task list.
    """
    sentences = tokenize_sentences(email_text)
    words = tokenize_words(email_text)
    freq = compute_word_freq(words)

    # Score each sentence based on word frequency
    sentence_scores = {}
    for sent in sentences:
        for word in tokenize_words(sent):
            if word in freq:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + freq[word]

    # Get top 3 sentences for summary
    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:3]
    summary = " ".join(top_sentences)

    # Extract actionable tasks
    tasks = extract_tasks(email_text)

    return {
        "summary": summary.strip(),
        "tasks": tasks
    }
