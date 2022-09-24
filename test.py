from node import Node 

def forward_test_1():
    output = Node(node_type = 2)
    children = [Node(children = [output]), Node(children = [output]), Node(children = [output])]
    i1 = Node(value = 1, node_type = 0, children = children)
    i2 = Node(value = 1, node_type = 0, children = children)
    i3 = Node(value = 1, node_type = 0, children = children)

    Node.forward([i1, i2, i3])

    print(f"i1: {i1.linear_value}")
    for node in i1.children:
        print(f"normalized value: {node.normalized_value}\tand value: {node.linear_value}")
    for node in i2.children:
        print(f"normalized value: {node.normalized_value}\tand value: {node.linear_value}")
    for node in i3.children:
        print(f"normalized value: {node.normalized_value}\tand value: {node.linear_value}")
    
    print(f"{output.linear_value}, {output.normalized_value}")

def backward_test_1():
    output = Node(node_type = 2)
    children = [Node(children = [output]), Node(children = [output]), Node(children = [output])]
    i1 = Node(value = 1, node_type = 0, children = children)
    i2 = Node(value = 1, node_type = 0, children = children)
    i3 = Node(value = 1, node_type = 0, children = children)

    Node.forward([i1, i2, i3])

    output.backward()
    layer_1 = []
    layer_2 = []
    for node in [i1, i2, i3]:
        layer_1.append(f"Layer 1 weights: {node.weights}")
        for last in node.children:
            layer_2.append(f"Layer 2 weights: {last.weights}")
    for t in layer_1+layer_2:
        print(t)

if __name__ == "__main__":
    forward_test_1()
    backward_test_1()