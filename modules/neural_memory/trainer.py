import torch
from torch.utils.data import DataLoader, TensorDataset
from modules.neural_memory.long_term_net import MemoryReinforcer

model = MemoryReinforcer()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
loss_fn = torch.nn.BCELoss()

def train_memory_model(data, labels, epochs=10):
    dataset = TensorDataset(data, labels)
    loader = DataLoader(dataset, batch_size=4, shuffle=True)

    for epoch in range(epochs):
        for x_batch, y_batch in loader:
            y_pred = model(x_batch)
            loss = loss_fn(y_pred, y_batch)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()