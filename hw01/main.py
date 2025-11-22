def build_graph(edges, directed=False):
    graph = {}

    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []

        graph[u].append(v)

        if not directed:
            graph[v].append(u)

    return graph


def degree_dict(graph):
    degree_map = {}

    for node, neighbors in graph.items():
        degree_map[node] = len(neighbors)

    return degree_map
