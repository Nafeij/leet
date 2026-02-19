# Topological Sort with Kahn's Algorithm

from collections import defaultdict, deque

# graph is represented as an adjacency list
def topological_sort(graph):
    in_degree = {u: 0 for u in graph}  # Initialize in-degrees of all vertices

    # Calculate in-degrees
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    # Queue for vertices with no incoming edges
    queue = deque([u for u in graph if in_degree[u] == 0])
    topo_order = []

    while queue:
        u = queue.popleft()
        topo_order.append(u)

        # Decrease the in-degree of neighboring vertices
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(topo_order) == len(graph):
        return topo_order  # Return the topological order if no cycle is detected
    else:
        raise ValueError("Graph has at least one cycle, topological sort not possible.")

if __name__ == '__main__':
    #              A   B
    #               \ / \
    #                C   D
    #                 \   \
    #                  E   |
    #                   \ /
    #                    F
    graph = {
        'A': ['C'],
        'B': ['C', 'D'],
        'C': ['E'],
        'D': ['F'],
        'E': ['F'],
        'F': []
    }
    try:
        order = topological_sort(graph)
        print("Topological Sort Order:", order)
    except ValueError as e:
        print(e)