import torch
from modules.neural_memory.trainer import train_memory_model
from modules.neural_memory.long_term_net import MemoryReinforcer

def feedback_to_training(feedback_memory):
    # einfache Vektorisierung: konzeptname → fixed index one-hot
    known = list({entry[0] for entry in feedback_memory})
    vecs = []
    labels = []
    for concept, score in feedback_memory:
        x = torch.zeros(len(known))
        x[known.index(concept)] = 1.0
        vecs.append(x)
        labels.append(torch.tensor([1.0 if score > 0 else 0.0]))

    data = torch.stack(vecs)
    targets = torch.stack(labels).float()
    train_memory_model(data, targets)
    return f"{len(vecs)} Feedbacks ins Modell integriert."