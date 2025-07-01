def create_intent(goal, mood, concept=None, related=None):
    if goal == "verknüpfen":
        return {
            "intent": "hypothesis",
            "confidence": 0.6 if mood == "curious" else 0.4,
            "target": concept,
            "action": "verknüpfen",
            "related": related,
            "goal": "validiere neues Konzept"
        }
    elif goal == "bestätigen":
        return {
            "intent": "assertion",
            "confidence": 0.9,
            "target": concept,
            "action": "festigen",
            "related": related,
            "goal": "stärke bestehendes Wissen"
        }
    return {
        "intent": "neutral",
        "confidence": 0.5,
        "target": concept,
        "action": "beobachten",
        "goal": "passiv analysieren"
    }