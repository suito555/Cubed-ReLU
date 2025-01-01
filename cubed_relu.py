import torch
from torch.nn import functional as F

def cubed_relu(x: torch.Tensor) -> torch.Tensor:
    return torch.pow(F.relu(x), 3) / 6
