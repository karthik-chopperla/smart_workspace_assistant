from typing import List, Dict
from utils.text_utils import tokenize_sentences, tokenize_words
from utils.vector_math import get_vector, cosine_similarity


def organize_notes(raw_text: str, similarity_threshold: float = 0.6) -> List[Dict[str, List[str]]]:
    """
    Dynamically clusters input notes into semantically similar groups.
    All logic, including topic generation, is derived from user input.
    """
    sentences = tokenize_sentences(raw_text)
    clusters = []

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue

        sentence_vec = get_vector(sentence)
        added_to_group = False

        for cluster in clusters:
            group_vec = get_vector(" ".join(cluster['items']))
            sim = cosine_similarity(sentence_vec, group_vec)
            if sim >= similarity_threshold:
                cluster['items'].append(sentence)
                added_to_group = True
                break

        if not added_to_group:
            clusters.append({'topic': None, 'items': [sentence]})

    # Purely dynamic topic generation — no hardcoded words or rules
    for cluster in clusters:
        word_freq = {}

        for sentence in cluster["items"]:
            for word in tokenize_words(sentence):
                word_freq[word] = word_freq.get(word, 0) + 1

        if word_freq:
            # Rank by frequency first, then by length — both from user input only
            top_words = sorted(
                word_freq.items(),
                key=lambda x: (-x[1], -len(x[0]))
            )[:2]

            cluster["topic"] = " ".join([word.capitalize() for word, _ in top_words])
        else:
            cluster["topic"] = "Notes"

    return clusters
