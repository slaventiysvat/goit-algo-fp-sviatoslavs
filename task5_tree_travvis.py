import uuid
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="#1a1a1a"):
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


def draw_tree(tree_root, title=""):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(9, 6))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def gradient_color(i: int, n: int) -> str:
    # dark blue -> light blue gradient (e.g. #1296F0 family)
    t = 0.0 if n <= 1 else i / (n - 1)
    r = int(18  + (180 - 18)  * t)
    g = int(80  + (210 - 80)  * t)
    b = int(144 + (255 - 144) * t)
    return f"#{r:02x}{g:02x}{b:02x}"


def dfs_order(root: Node) -> list[Node]:
    order = []
    stack = [root]
    visited = set()
    while stack:
        cur = stack.pop()
        if cur.id in visited:
            continue
        visited.add(cur.id)
        order.append(cur)
        # to have left first — push right, then left
        if cur.right: stack.append(cur.right)
        if cur.left: stack.append(cur.left)
    return order


def bfs_order(root: Node) -> list[Node]:
    order = []
    q = deque([root])
    visited = set()
    while q:
        cur = q.popleft()
        if cur.id in visited:
            continue
        visited.add(cur.id)
        order.append(cur)
        if cur.left: q.append(cur.left)
        if cur.right: q.append(cur.right)
    return order


def colorize_by_order(root: Node, order: list[Node]) -> None:
    n = len(order)
    for i, node in enumerate(order):
        node.color = gradient_color(i, n)


if __name__ == "__main__":
    # test three
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    # DFS
    order = dfs_order(root)
    colorize_by_order(root, order)
    draw_tree(root, title="DFS traversal coloring")

    # BFS (reset colors)
    for n in bfs_order(root):
        n.color = "#1a1a1a"
    order = bfs_order(root)
    colorize_by_order(root, order)
    draw_tree(root, title="BFS traversal coloring")