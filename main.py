import torch

my_torch = torch.arange(10)
print(my_torch)

# my_torch.reshape(2, 6) # doesn't work! Intentional, the number pair doesn't equal to 10, 2 x 6 = 12, not 10

my_torch2 = torch.arange(10)
print(my_torch2)

my_torch2 = my_torch2.reshape(2, -1)
print(my_torch2)

my_torch3 = torch.arange(10)
print(my_torch3)

my_torch4 = my_torch3.view(2, 5)
print(my_torch4)

# When you use reshape or view, the tensor will update

my_torch5 = torch.arange(10)
print(my_torch5)

my_torch6 = my_torch5.reshape(2, 5)
print(my_torch6)

my_torch5[1] = 1234  # my_torch6 will update if we print it out after we change the value.
print(my_torch5)
print(my_torch6)

# Slices
my_torch7 = torch.arange(10)
print(my_torch7)

# Grab a specific item
print(my_torch7[7])

# Grab a slice
my_torch8 = my_torch7.reshape(5, 2)
print(my_torch8)

# Returns Row
print(my_torch8[:, 1])

# Returns Column
print(my_torch8[:, 1:])
