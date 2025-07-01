import tkinter as tk
from tkinter import simpledialog
from modules.rewards.feedback_engine import register_feedback

def ask_feedback(response, concept=""):
    root = tk.Tk()
    root.withdraw()
    rating = simpledialog.askstring("Feedback", f"Wie bewertest du diese Antwort?\n'{response}'\n(z. B. gut, schlecht, unsicher)")
    comment = simpledialog.askstring("Kommentar", "Optionaler Kommentar?")
    if rating:
        result = register_feedback(concept or response, 1.0 if rating == "gut" else -1.0 if rating == "schlecht" else 0.0)
        return f"💬 Feedback: {rating} ({comment}) → {result}"
    return "⚠️ Kein Feedback erteilt."