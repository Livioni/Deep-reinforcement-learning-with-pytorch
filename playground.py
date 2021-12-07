import torch
from collections import namedtuple
from torch.utils.data.sampler import BatchSampler, SubsetRandomSampler
import numpy as np

Transition = namedtuple('Transition', ['state', 'action', 'reward', 'next_state'])#有点像结构体定义
memory = [None]*10
transition = Transition(1,3,3,5)
memory[0] = transition
# print(memory[0])
# print(memory[1])
memory[0].reward

list = np.array([[1,2,3],[4,5,6],[7,8,9]])
list[2, :] = np.array([1,2,3])
print(list)