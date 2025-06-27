from utils.storage import update_feedback_state


def update_logic_based_on_feedback(feedback: dict):
    """
    Simulates adaptive learning by adjusting parameters or thresholds based on user feedback.
    This function avoids model training but uses logic updates dynamically.
    """

    # Simulated parameter updates
    adjustments = {}

    if feedback["summary"] < 3:
        adjustments["summary_sentences"] = 2
    else:
        adjustments["summary_sentences"] = 3

    if feedback["tasks"] < 3:
        adjustments["task_threshold"] = 0.3
    else:
        adjustments["task_threshold"] = 0.5

    if feedback["schedule"] < 3:
        adjustments["urgency_bias"] = -1
    else:
        adjustments["urgency_bias"] = 0

    if feedback["notes"] < 3:
        adjustments["group_similarity"] = 0.3
    else:
        adjustments["group_similarity"] = 0.5

    # Persist feedback logic state
    update_feedback_state(adjustments)
