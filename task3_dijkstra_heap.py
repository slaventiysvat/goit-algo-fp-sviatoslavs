import heapq
from typing import Dict, List, Tuple, Any


Graph = Dict[Any, List[Tuple[Any, float]]]  # node -> [(neighbor, weight)]


def dijkstra(graph: Graph, start) -> Dict[Any, float]:
    dist = {node: float("inf") for node in graph}
    dist[start] = 0.0

    pq = [(0.0, start)]  # (distance, node)

    while pq:
        cur_dist, u = heapq.heappop(pq)
        if cur_dist > dist[u]:
            continue

        for v, w in graph[u]:
            nd = cur_dist + w
            if nd < dist.get(v, float("inf")):
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    return dist


if __name__ == "__main__":
    graph: Graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("A", 1), ("C", 2), ("D", 5)],
        "C": [("A", 4), ("B", 2), ("D", 1)],
        "D": [("B", 5), ("C", 1)],
    }

    start = "A"
    distances = dijkstra(graph, start)
    print("Shortest paths from", start)
    for node, d in distances.items():
        print(f"  {node}: {d}")