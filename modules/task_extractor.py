import re
from typing import List
from utils.text_utils import tokenize_sentences, tokenize_words


def extract_tasks_from_summary(summary: str) -> List[str]:
    """
    Extracts task-like statements from a summary using rule-based AI logic.
    Detects action verbs, dates, and important phrasing patterns.
    """
    if not summary.strip():
        return []

    # Define basic patterns dynamically
    action_verbs = ['submit', 'complete', 'send', 'schedule', 'review', 'prepare', 'finalize', 'respond']
    date_patterns = [
        r'\bby\s+(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\b',
        r'\bby\s+\d{1,2}(st|nd|rd|th)?\b',
        r'\bon\s+(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\b',
        r'\bon\s+\d{1,2}/\d{1,2}/\d{2,4}\b',
        r'\btomorrow\b', r'\bnext week\b', r'\bby end of day\b'
    ]

    tasks = []
    sentences = tokenize_sentences(summary)

    for sent in sentences:
        words = tokenize_words(sent.lower())

        # Identify if sentence contains an action verb
        if any(verb in words for verb in action_verbs):
            tasks.append(sent)
            continue

        # Identify if sentence contains date/time patterns
        for pattern in date_patterns:
            if re.search(pattern, sent, re.IGNORECASE):
                tasks.append(sent)
                break

    return tasks
