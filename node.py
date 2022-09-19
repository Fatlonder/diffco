from typing import List
from collections import deque
partials_node = {}

class Node:
    weights: List[float]
    children: List['Node']
    backward_children: List['Node'] # If memory becomes an issue we will use only the above relation list for forward and backward. 
    linear_value: float
    normalized_value:float

    partial_values: List[float]
    fn: lambda x: x
    node_type: float # 0 - Input node, 1 - Intermediate node, 2 - Terminal node. 
    node_grad: float # partial of fn w.r.t children in backward phase. 

    def __init__(self, value: float = 0, node_type:float = 1, children: List[any] = []): # Type of children is ComputingNode
        self.children = children
        self.node_type = node_type
        self.weights = []
        self.backward_children = []
        self.partial_values = []
        self._random_weight()
        self.linear_value = value
        self.fn = lambda x: x**2
        self.normalized_value = value if self.node_type == 0 else self.fn(value) # Why now?

    def _random_weight(self):
        if self.children is not None:
            for i in range(len(self.children)): self.weights.append(1) 

    def backprop(self):
        # TODO
        print(self)

    @staticmethod
    def forward(input: List['Node']):
        node_queue = deque(input)
        while len(node_queue)>0:
            parent = node_queue.popleft()
            if parent.node_type != 0:
                parent.linear_value = sum(parent.partial_values)
                parent.normalized_value = parent.fn(parent.linear_value)
            j = 0
            for child in parent.children:
                child.backward_children.append(parent)
                child.partial_values.append(parent.normalized_value*parent.weights[j]) # For terminal nodes we don't multiply by the weight. 
                if node_queue.count(child) == 0: node_queue.append(child) 
                j+=1