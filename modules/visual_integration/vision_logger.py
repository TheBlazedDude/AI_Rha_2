import json
import os

log_path = "data/vision_log/vision.json"

def log_vision_entry(entry):
    if os.path.exists(log_path):
        with open(log_path, "r") as f:
            data = json.load(f)
    else:
        data = []
    data.append(entry)
    with open(log_path, "w") as f:
        json.dump(data, f, indent=2)