import torch
import torch.nn as nn
import torch.nn.functional as F

class MemoryReinforcer(nn.Module):
    def __init__(self, input_dim=10, hidden_dim=32, output_dim=1):
        super(MemoryReinforcer, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        return torch.sigmoid(self.fc2(x))