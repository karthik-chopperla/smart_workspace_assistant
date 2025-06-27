from utils.text_utils import tokenize_sentences, tokenize_words, compute_word_freq
from modules.task_extractor import extract_tasks

def summarize_email(email_text: str) -> dict:
    """
    Summarizes an email and extracts actionable tasks.
    Returns a dictionary with 'summary' and 'tasks'.
    """

    # Tokenize input text
    sentences = tokenize_sentences(email_text)
    words = tokenize_words(email_text)
    freq = compute_word_freq(words)

    # Score sentences by frequency of important words
    sentence_scores = {}
    for sentence in sentences:
        for word in tokenize_words(sentence):
            if word in freq:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + freq[word]

    # Select top 3 highest-scoring sentences
    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:3]
    summary = " ".join(top_sentences).strip()

    # Extract tasks using the task extractor module
    tasks = extract_tasks(email_text)

    return {
        "summary": summary,
        "tasks": tasks
    }
