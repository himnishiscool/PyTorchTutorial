import torch
import torch.nn as nn
import torch.nn.functional as F

# Create a Model Class that inherits nn.Module


class Model(nn.Module):
    # Input layer (4 features of the flower) -->
    # Hidden Layer 1 (Number of neurons) -->
    # Hidden Layer 2 (Number of Neurons) -->
    # Output (3 types of Iris flowers)

    def __init__(self, input_features=4, h1=8, h2=8, output_features=3):
        # instantiate out __init__
        super().__init__()
        # FC means FULLY CONNECTED
        self.fc1 = nn.Linear(input_features, h1)
        self.fc2 = nn.Linear(h1, h2)
        self.out = nn.Linear(h2, output_features)

    def forward(self, x):
        # Moves FORWARD through each FULLY CONNECTED LAYER, then the OUTPUT
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.out(x)

        return x


# Pick a manual seed for RANDOMIZATION
# Why is because we NEED to TELL it WHERE TO START BEFORE RANDOMIZATION
torch.manual_seed(41)

model = Model()
