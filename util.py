from typing import List

def toposort(node_list: List['Node']):
    sorted_graph = [node for node in node_list]
    for node in sorted_graph:
        yield node
        for child in node.backward_children:
            if (sorted_graph.count(child)) == 0:
                sorted_graph.append(child)