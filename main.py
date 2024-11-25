import torch

tensor_a = torch.tensor([1, 2, 3, 4])
tensor_b = torch.tensor([5, 6, 7, 8])

# Addition
print(tensor_a + tensor_b)

# Addition Longhand
print(torch.add(tensor_a, tensor_b))

# Subtraction
print(tensor_b - tensor_a)

# Subtraction Longhand
print(torch.sub(tensor_b, tensor_a))
print(torch.subtract(tensor_b, tensor_a))

# Multiplication
print(tensor_a * tensor_b)

# Multilplication Longhand
print(torch.mul(tensor_a, tensor_b))
print(torch.multiply(tensor_a, tensor_b))

# Division
print(tensor_b / tensor_a)

# Division Longhand
print(torch.div(tensor_b, tensor_a))
print(torch.divide(tensor_b, tensor_a))

# Modulus / Remainders
print(tensor_b % tensor_a)

# Modulus / Remainders Longhand
print(torch.remainder(tensor_b, tensor_a))

# Exponents
print(tensor_a ** tensor_b)

# Exponents Longhand
print(torch.pow(tensor_a, tensor_b))

# Another way to write Longhand Operations, but SHORT TERM. Does NOT save operation in tensor_a
tensor_a.add(tensor_b)
tensor_a.sub(tensor_b)
tensor_a.subtract(tensor_b)
tensor_a.mul(tensor_b)
tensor_a.multiply(tensor_b)
tensor_a.div(tensor_b)
tensor_a.divide(tensor_b)
tensor_a.remainder(tensor_b)
tensor_a.pow(tensor_b)

# Another way to write Longhand Operations, but LONG TERM. DOES save operation in tensor_a
tensor_a.add_(tensor_b)
tensor_a.sub_(tensor_b)
tensor_a.subtract_(tensor_b)
tensor_a.mul_(tensor_b)
tensor_a.multiply_(tensor_b)
tensor_a.div_(tensor_b)
tensor_a.divide_(tensor_b)
tensor_a.remainder_(tensor_b)
tensor_a.pow_(tensor_b)
