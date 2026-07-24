import heapq

# Graph representation
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

# Heuristic values (estimated cost to goal F)
heuristic = {
    'A': 5,
    'B': 3,
    'C': 4,
    'D': 6,
    'E': 1,
    'F': 0
}

# A* Algorithm
def a_star(start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start, [start]))
    
    visited = set()

    while open_list:
        f, current, path = heapq.heappop(open_list)

        if current == goal:
            return path, f

        if current in visited:
            continue

        visited.add(current)

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                g = f - heuristic[current] + cost
                h = heuristic[neighbor]
                heapq.heappush(open_list, (g + h, neighbor, path + [neighbor]))

    return None, None

# -------- MAIN --------
path, cost = a_star('A', 'F')

print("Path found:", path)
print("Total cost:", cost)
