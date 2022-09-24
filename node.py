from typing import List
import math
from util import toposort

class Node(object):
    weights: List[float]
    children: List['Node']
    backward_children: List['Node'] # If memory becomes an issue we will use only the above relation list for forward and backward. 
    linear_value: float
    normalized_value:float
    partial_values: List[float]
    fn: lambda x: 1/(1+math.e**(-1*x))
    gradient_fn: lambda x: x
    lr: float
    node_type: float # 0 - Input node, 1 - Intermediate node, 2 - Terminal node. 
    chain_accum_prod: float
    chain_accum: List[float]
    weight_index: float

    def __init__(self, value: float = 0, node_type:float = 1, children: List[any] = [], lr: float = 0.001):
        self.children = children
        self.node_type = node_type
        self.weights = []
        self.backward_children = []
        self.partial_values = []
        self._random_weight()
        self.linear_value = value
        self.fn = lambda x: 1/(1+math.e**(-1*x))
        self.gradient_fn = lambda x: self.fn(x) * (1 - self.fn(x)) 
        self.normalized_value = value
        self.lr = lr
        self.chain_accum_prod = 0
        self.chain_accum = []
        self.weight_index = 0

    def _random_weight(self):
        if self.children is not None:
            for i in range(len(self.children)): self.weights.append(1) # Make it at least pseudo-random

    def backward(self):
        node_queue = toposort([self]+ self.backward_children, type='backward')
        for current in node_queue:
            current.chain_accum_prod = 1
            current.weight_index = 0
            if current.node_type != 2:
                current.chain_accum_prod = sum(current.chain_accum)
            for child in current.backward_children:
                i = child.weight_index
                accumulated_gradients = current.chain_accum_prod * current.gradient_fn(current.linear_value) # Construct a table that maps functions to derivatives. 
                child.chain_accum.append(accumulated_gradients * child.weights[i])
                delta_w = accumulated_gradients * child.normalized_value
                child.weights[i] = child.weights[i] - current.lr*delta_w
                child.weight_index +=1

    @staticmethod
    def forward(input: List['Node']):
        node_queue = toposort(input)
        for parent in node_queue:
            if parent.node_type != 0:
                parent.linear_value = sum(parent.partial_values)
                parent.normalized_value = parent.fn(parent.linear_value)
            j = 0
            for child in parent.children:
                child.backward_children.append(parent)
                child.partial_values.append(parent.normalized_value*parent.weights[j])
                j+=1