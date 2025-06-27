import numpy as np
from utils.text_utils import clean_text, tokenize_words


def get_vector(text: str, dim: int = 50):
    """
    Simulates a semantic vector using word hashes and position weighting.
    Still works without any ML libraries or external APIs.
    """
    words = tokenize_words(text)
    vec = np.zeros(dim)

    for i, word in enumerate(words):
        # Create a stable pseudo-random vector using hash
        seed = abs(hash(word)) % (10 ** 6)
        rng = np.random.default_rng(seed)
        word_vec = rng.standard_normal(dim)

        # Weighted average by position (simulate semantic shift)
        weight = 1 / (1 + i)
        vec += weight * word_vec

    # Normalize the vector
    norm = np.linalg.norm(vec)
    return vec / norm if norm != 0 else vec


def cosine_similarity(v1, v2):
    """
    Cosine similarity between two vectors.
    """
    if np.linalg.norm(v1) == 0 or np.linalg.norm(v2) == 0:
        return 0.0
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
