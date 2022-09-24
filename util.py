from typing import List

def toposort(node_list: List['Node'], type = 'forward'):
    sorted_graph = [node for node in node_list]
    for node in sorted_graph:
        yield node
        children = node.children if type == 'forward' else node.backward_children
        for child in children:
            if (sorted_graph.count(child)) == 0:
                sorted_graph.append(child)