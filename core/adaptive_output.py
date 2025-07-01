import random

templates = {
    "definition": [
        "{X} ist ein {Y}.",
        "Man kann sagen, dass {X} zur Kategorie {Y} gehört.",
        "Im Allgemeinen zählt {X} zu den {Y}."
    ],
    "question": [
        "Ist {X} möglicherweise ein {Y}?",
        "Kann man {X} als {Y} betrachten?",
        "Gehört {X} vielleicht zu {Y}?"
    ]
}

def generate_adaptive_sentence(X, Y, mode="definition"):
    return random.choice(templates.get(mode, ["{X} ist {Y}."])).format(X=X, Y=Y)