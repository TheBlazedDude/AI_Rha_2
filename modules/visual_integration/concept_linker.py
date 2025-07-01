from core.knowledge_graph import _load_knowledge

def propose_concepts(objects):
    known = _load_knowledge()
    suggestions = []
    for obj in objects:
        if obj not in known:
            suggestions.append(f"Ich sehe '{obj}'. Ist das ein neues Konzept?")
    return suggestions