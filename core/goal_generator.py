def generate_goals(mood, memory):
    if mood == "curious":
        return ["Finde neue Konzepte", "Teste Zusammenhang von Ideen"]
    elif mood == "tired":
        return ["Reduziere interne Aktivität", "Nur Wichtiges prüfen"]
    return ["Verstärke bekannte Fakten", "Stelle neue Hypothesen"]