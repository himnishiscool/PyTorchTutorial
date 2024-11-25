import torch
import numpy as np

my_list = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
]
np1 = np.random.rand(3, 4)
tensor = torch.randn(3, 4)
tensor_3d = torch.zeros(2, 3, 4)

my_tensor = torch.tensor(np1)

print(my_list)
print(np1)
print(tensor)
print(tensor_3d)

print(my_tensor)
