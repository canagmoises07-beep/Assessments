# Assessment 3.3: Non-Linear Data Structure
# Graph using the letters of CANAG
#
# A2 means the second occurrence of the letter A.
#
#       C
#      / \
#     A---N
#     |   |
#     G---A2
#
# Edges: C-A, C-N, A-N, A-G, N-A2, G-A2

graph = {
    "C":  ["A", "N"],
    "A":  ["C", "G", "N"],
    "N":  ["C", "A", "A2"],
    "G":  ["A", "A2"],
    "A2": ["N", "G"]
}


def bfs(graph, start):
    """Breadth-First Search: visit neighboring vertices level by level."""
    visited = {start}
    queue = [start]
    result = []

    while queue:
        current = queue.pop(0)
        result.append(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


def dfs(graph, start):
    """Depth-First Search: follow a path deeply before backtracking."""
    visited = set()
    result = []

    def visit(vertex):
        visited.add(vertex)
        result.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visit(neighbor)

    visit(start)
    return result


print("GRAPH TRAVERSAL")
print("BFS:", " - ".join(bfs(graph, "C")))
print("DFS:", " - ".join(dfs(graph, "C")))
