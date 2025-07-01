import tkinter as tk
from tkinter import simpledialog, messagebox
from modules.rewards.feedback_engine import feedback_memory

def show_feedback_manager():
    win = tk.Toplevel()
    win.title("Letzte Feedbacks")

    feedback_listbox = tk.Listbox(win, width=100)
    feedback_listbox.pack(padx=10, pady=5)

    for i, entry in enumerate(feedback_memory[-20:]):
        feedback_listbox.insert(tk.END, f"{i+1}. {entry[0]} → {entry[1]}")

    def on_select(event):
        selection = feedback_listbox.curselection()
        if not selection:
            return
        index = selection[0]
        full_entry = feedback_memory[-20:][index]
        concept, score = full_entry

        edit_win = tk.Toplevel(win)
        edit_win.title("Feedback bearbeiten")

        tk.Label(edit_win, text="Konzept:").pack()
        concept_entry = tk.Entry(edit_win, width=50)
        concept_entry.pack()
        concept_entry.insert(0, concept)

        tk.Label(edit_win, text="Score (-1.0 bis 1.0):").pack()
        score_entry = tk.Entry(edit_win, width=20)
        score_entry.pack()
        score_entry.insert(0, str(score))

        def save_edit():
            try:
                new_score = float(score_entry.get())
                new_concept = concept_entry.get()
                feedback_memory[-20:][index] = (new_concept, new_score)
                feedback_listbox.delete(index)
                feedback_listbox.insert(index, f"{index+1}. {new_concept} → {new_score}")
                messagebox.showinfo("Aktualisiert", "Feedback wurde geändert.")
                edit_win.destroy()
            except Exception as e:
                messagebox.showerror("Fehler", str(e))

        def delete_entry():
            del feedback_memory[-20:][index]
            feedback_listbox.delete(index)
            messagebox.showinfo("Gelöscht", "Feedback wurde gelöscht.")
            edit_win.destroy()

        tk.Button(edit_win, text="Speichern", command=save_edit).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(edit_win, text="Löschen", command=delete_entry).pack(side=tk.RIGHT, padx=10, pady=10)

    feedback_listbox.bind("<<ListboxSelect>>", on_select)