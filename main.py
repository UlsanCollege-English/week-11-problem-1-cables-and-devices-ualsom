"""
HW01 — Cables and Devices

Implement:
- build_graph(edges, directed=False)
- degree_dict(graph)

Do NOT add type hints. Use only the standard library.
"""

def build_graph(edges, directed=False):
    """Return a dictionary: node -> list of neighbors.

    edges: list of (u, v) pairs.
    directed: if True, add only u->v; if False, add both u->v and v->u.
    """
    graph = {}

    for u, v in edges:
        # Ensure nodes exist
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []

        # Add u -> v
        graph[u].append(v)

        # If undirected, also add v -> u
        if not directed:
            graph[v].append(u)

    return graph


def degree_dict(graph):
    """Return a dictionary: node -> degree (number of neighbors).

    For directed graphs, this is out-degree.
    For undirected graphs, this is the usual degree.
    """
    degree_map = {}

    for node, neighbors in graph.items():
        degree_map[node] = len(neighbors)

    return degree_map
