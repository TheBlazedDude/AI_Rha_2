from core.speech_intent import create_intent
from core.intent_to_sentence import verbalize_intent

class GoalExecutor:
    def __init__(self, state):
        self.state = state

    def execute(self, goal, concept, related):
        intent = create_intent(goal, self.state.get("mood", "neutral"), concept, related)
        sentence = verbalize_intent(intent, self.state.get("mood", "neutral"))
        self.state["last_intent"] = intent["intent"]
        self.state["last_strategy"] = intent.get("strategy", "-")
        return sentence