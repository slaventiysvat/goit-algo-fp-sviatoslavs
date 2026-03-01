import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(9, 6))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def heap_to_tree(heap: list[int]) -> Node | None:
    if not heap:
        return None

    nodes = [Node(v) for v in heap]
    for i in range(len(nodes)):
        li = 2 * i + 1
        ri = 2 * i + 2
        if li < len(nodes):
            nodes[i].left = nodes[li]
        if ri < len(nodes):
            nodes[i].right = nodes[ri]
    return nodes[0]


def draw_heap(heap: list[int]) -> None:
    root = heap_to_tree(heap)
    if root is None:
        print("Heap is empty")
        return
    draw_tree(root)


if __name__ == "__main__":
    heap = [1, 3, 2, 7, 6, 4, 5]  # example of min-heap (or any heap)
    draw_heap(heap)