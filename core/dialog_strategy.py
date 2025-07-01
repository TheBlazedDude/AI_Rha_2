def choose_strategy(intent, mood):
    if intent["intent"] == "hypothesis":
        if mood == "curious":
            return "fragend"
        else:
            return "vorsichtig"
    elif intent["intent"] == "assertion":
        if mood == "confident":
            return "erklärend"
        else:
            return "neutral"
    return "minimal"