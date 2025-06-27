from utils.text_utils import tokenize_sentences, tokenize_words, compute_word_freq, extract_tasks

def summarize_email(email_text: str) -> dict:
    # Break email into sentences
    sentences = tokenize_sentences(email_text)
    words = tokenize_words(email_text)
    
    # Compute word frequency
    freq = compute_word_freq(words)

    # Score each sentence
    sentence_scores = {}
    for sentence in sentences:
        word_list = tokenize_words(sentence)
        score = sum(freq.get(word.lower(), 0) for word in word_list)
        sentence_scores[sentence] = score

    # Take top 3 highest scoring sentences
    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:3]
    summary = " ".join(top_sentences).strip()

    # Extract tasks
    tasks = extract_tasks(email_text)

    return {
        "summary": summary,
        "tasks": tasks
    }
