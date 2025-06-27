from utils.text_utils import tokenize_sentences, tokenize_words, compute_word_freq, extract_tasks

def summarize_email(email_text, max_sentences=3):
    sentences = tokenize_sentences(email_text)
    words = tokenize_words(email_text)
    freq = compute_word_freq(words)

    # Score sentences based on word frequency
    scored_sentences = []
    for sentence in sentences:
        word_list = tokenize_words(sentence)
        score = sum(freq.get(word, 0) for word in word_list)
        scored_sentences.append((score, sentence))

    # Sort and select top sentences
    top_sentences = [s for _, s in sorted(scored_sentences, reverse=True)[:max_sentences]]
    summary = " ".join(top_sentences).strip()

    # Extract actionable tasks
    tasks = extract_tasks(email_text)

    return {
        "summary": summary,
        "tasks": tasks
    }
