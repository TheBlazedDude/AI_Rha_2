def analyze_contradictions(graph):
    contradictions = []
    for node, edges in graph.items():
        if "Tier" in edges and "Pflanze" in edges:
            contradictions.append(f"Widerspruch bei {node}: Tier und Pflanze gleichzeitig.")
    return contradictions