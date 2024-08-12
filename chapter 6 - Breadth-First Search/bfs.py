# useful for one thing finding the shortest path on unweighted graphs
# O(V + E)
def bfs(graph, node):

    visited = []
    queue = [node]

    while queue:
        item = queue.pop(0)
        if item not in visited:
            print(item, end=" ")
            visited.append(item)
            queue += graph[item]
