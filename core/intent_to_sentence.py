from core.adaptive_output import generate_adaptive_sentence
from core.dialog_strategy import choose_strategy

def verbalize_intent(intent, mood):
    style = choose_strategy(intent, mood)
    X = intent.get("target", "X")
    Y = intent.get("related", "Y")
    if intent["intent"] == "hypothesis":
        return generate_adaptive_sentence(X, Y, mode="question")
    elif intent["intent"] == "assertion":
        return generate_adaptive_sentence(X, Y, mode="definition")
    return f"{X} steht in Beziehung zu {Y}."