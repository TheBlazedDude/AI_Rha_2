feedback_memory = []

def register_feedback(concept, score):
    feedback_memory.append((concept, score))
    return f"Feedback für {concept} erhalten: {score}"