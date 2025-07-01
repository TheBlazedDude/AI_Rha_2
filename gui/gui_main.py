from gui.feedback_manager import show_feedback_manager
import tkinter as tk
from tkinter import messagebox, scrolledtext
import threading
import time

from core.agent_core import AIAgent
from modules.speech.tts_engine import enable_tts, speak
from modules.vision.vision_core import enable_vision
from modules.self_learning.optimizer import optimize_knowledge
from modules.reading.reader import read_txt_folder

class AIGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI-RHA Control Interface")
        self.agent = AIAgent()
        self.running = False
        self.setup_ui()

    def setup_ui(self):
        # Textanzeige
        self.output_box = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, height=20, width=80)
        self.output_box.pack(padx=10, pady=5)

        # Eingabezeile
        self.input_entry = tk.Entry(self.root, width=60)
        self.input_entry.pack(side=tk.LEFT, padx=10)
        self.input_entry.bind("<Return>", self.process_input)

        self.send_btn = tk.Button(self.root, text="Senden", command=self.process_input)
        self.send_btn.pack(side=tk.LEFT)

        # Kontroll-Checkboxes
        self.speech_var = tk.BooleanVar()
        self.vision_var = tk.BooleanVar()

        self.speech_cb = tk.Checkbutton(self.root, text="Sprache aktivieren", var=self.speech_var, command=self.toggle_speech)
        self.speech_cb.pack(anchor="w", padx=10)

        self.vision_cb = tk.Checkbutton(self.root, text="Kamera aktivieren", var=self.vision_var, command=self.toggle_vision)
        self.vision_cb.pack(anchor="w", padx=10)

        
        # Statusanzeige (Mood, Strategie, Intent)
        self.status_frame = tk.Frame(self.root)
        self.status_frame.pack(pady=10)

        self.mood_label = tk.Label(self.status_frame, text="Mood: neutral", anchor="w")
        self.mood_label.grid(row=0, column=0, sticky="w", padx=5)

        self.intent_label = tk.Label(self.status_frame, text="Intent: -", anchor="w")
        self.intent_label.grid(row=0, column=1, sticky="w", padx=5)

        self.strategy_label = tk.Label(self.status_frame, text="Strategie: -", anchor="w")
        self.strategy_label.grid(row=0, column=2, sticky="w", padx=5)
\n        # Buttons
        self.optimize_btn = tk.Button(self.root, text="Selbstoptimierung", command=self.optimize)
        self.optimize_btn.pack(pady=5)

        self.reader_btn = tk.Button(self.root, text="Lektüre (TXT lesen)", command=self.read_txt)
        self.reader_btn.pack(pady=5)

        self.start_btn = tk.Button(self.root, text="Start KI-Zyklus", command=self.start_agent)
        self.start_btn.pack(pady=5)

        self.stop_btn = tk.Button(self.root, text="Stop", command=self.stop_agent)
        
        self.train_btn = tk.Button(self.root, text="Feedback → Lernen", command=self.train_from_feedback)
        self.train_btn.pack(pady=5)
        self.feedback_mgmt_btn = tk.Button(self.root, text="Feedback-Verwaltung", command=show_feedback_manager)
        self.feedback_mgmt_btn.pack(pady=5)

        self.stop_btn.pack(pady=5)

    def append_output(self, text):
        self.output_box.insert(tk.END, text + "\n")
        self.output_box.see(tk.END)
        if self.speech_var.get():
            speak(text)

    def process_input(self, event=None):
        user_input = self.input_entry.get()
        if not user_input:
            return
        self.append_output("👤 " + user_input)
        self.input_entry.delete(0, tk.END)
        response = self.agent.process_input(user_input)
        self.append_output("🤖 " + response)\n        with open("logs/full_interaction_log.json", "a", encoding="utf-8") as f:
            import json
            log_entry = {
                "user_input": user_input,
                "ai_response": response,
                "mood": self.agent.state.get("mood", "-"),
                "intent": getattr(self.agent, "last_intent", "-"),
                "strategy": getattr(self.agent, "last_strategy", "-")
            }
            f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")\n        self.update_status(
            self.agent.state.get("mood", "-"),
            getattr(self.agent, "last_intent", "-"),
            getattr(self.agent, "last_strategy", "-")
        )

    def toggle_speech(self):
        if self.speech_var.get():
            enable_tts()
            self.append_output("[Sprachausgabe aktiviert]")

    def toggle_vision(self):
        if self.vision_var.get():
            enable_vision()
            self.append_output("[Kameraeinspeisung aktiviert]")

    def optimize(self):
        result = optimize_knowledge()
        self.append_output("[Optimierung]: " + result)

    def read_txt(self):
        results = read_txt_folder()
        self.append_output(f"[Lektüre abgeschlossen] {len(results)} neue Einträge.")

    def start_agent(self):
        if not self.running:
            self.append_output("[KI-Denkzyklen gestartet]")
            self.agent.boot()
            self.running = True
            threading.Thread(target=self.run_loop, daemon=True).start()

    def stop_agent(self):
        self.running = False
        self.append_output("[KI-Zyklus gestoppt]")

    def run_loop(self):
        while self.running and self.agent.active:
            self.agent.run_cycle()
            time.sleep(1)

if __name__ == "__main__":
    root = tk.Tk()
    app = AIGUI(root)
    root.mainloop()\n\n
    def update_status(self, mood, intent_text, strategy):
        self.mood_label.config(text=f"Mood: {mood}")
        self.intent_label.config(text=f"Intent: {intent_text}")
        self.strategy_label.config(text=f"Strategie: {strategy}")



    def train_from_feedback(self):
        from modules.rewards.reward_adapter import feedback_to_training
        from modules.rewards.feedback_engine import feedback_memory
        result = feedback_to_training(feedback_memory)
        self.append_output("[Training]: " + result)
