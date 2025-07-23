import torch

a = torch.randn((10000, 10000))
b = torch.randn((10000, 2000))

c = a @ b

print(c.shape)
