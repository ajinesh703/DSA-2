from collections import deque

def shortest_path(graph, start, end):
    queue = deque([(start, [start])])  # (node, path)
    visited = set()
    
    while queue:
        node, path = queue.popleft()
        if node == end:
            return path
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    
    return None  # No path exists
