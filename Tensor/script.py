import numpy as np
import torch

arr = np.array([1,2,3,4,5])
arr.dtype
x = torch.from_numpy(arr)

torch.as_tensor(arr)

arr2d = np.arange(0.0, 12.0)
arr2d = arr2d.reshape(4,3)

x2 = torch.from_numpy(arr2d)
arr[0] = 99
x

my_arr = np.arange(0, 10)
my_tensor = torch.tensor(my_arr)
my_other_tensor = torch.from_numpy(my_arr)

my_arr[0] = 9999

my_tensor
my_other_tensor

### Unterschiede tensor vs Tensor
new_arr = np.array([1,2,3,4,5])

torch.tensor(new_arr)
torch.Tensor(new_arr)

torch.empty(4,2, dtype=torch.int32)
torch.zeros(4,3, dtype=torch.int64)

torch.arange(0,18,2).reshape(3,3)
torch.linspace(0, 18,12).reshape(3,4)
torch.rand(4,3)
torch.randn(1000, 1000)

# Tensor Operationen
x = torch.arange(6).reshape(3,2)
x[:,1:2]
x[:1,:]


x = torch.arange(100)
x

x.view(5, 20)
x.view(-1, 10) #-1 für jeden Wert den man durch 100 teilen kann

a = torch.tensor([1,2,3,4])
b = torch.tensor([2,4,5,1])

torch.add(a,b)

a.add_(b)

### 
x = torch.tensor(2.0, requires_grad=True)

y = 2*x**4 + x**3 +  3*x**2 + 5*x + 1
y.backward()
x.grad



