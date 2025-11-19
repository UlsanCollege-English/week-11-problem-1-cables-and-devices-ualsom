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

        # Ensure the node 'u' exists
        if u not in graph:
            graph[u] = []

        # Ensure the node 'v' exists (important for directed graphs)
        if v not in graph:
            graph[v] = []

        # Add edge u -> v
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


if __name__ == "__main__":
    # Manual testing
    sample = [('PC1','SW1'), ('SW1','PR1'), ('PR1','PC2')]
    print("Sample edges:", sample)

    # Undirected
    g_undirected = build_graph(sample, directed=False)
    print("\n--- Undirected Graph ---")
    print("Graph:", g_undirected)
    print("Degrees:", degree_dict(g_undirected))

    # Directed
    sample_directed = [('A', 'B'), ('B', 'C'), ('A', 'C')]
    g_directed = build_graph(sample_directed, directed=True)
    print("\n--- Directed Graph ---")
    print("Graph:", g_directed)
    print("Degrees:", degree_dict(g_directed))
