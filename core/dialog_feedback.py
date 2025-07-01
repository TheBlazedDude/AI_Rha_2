feedback_store = []

def rate_response(response, rating, comment=None):
    entry = {
        "response": response,
        "rating": rating,
        "comment": comment
    }
    feedback_store.append(entry)
    return f"Feedback gespeichert: {rating}"