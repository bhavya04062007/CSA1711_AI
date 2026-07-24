from collections import deque

# Capacities of jugs
JUG1 = 4
JUG2 = 3

# Goal
GOAL = 2

# BFS to solve Water Jug Problem
def water_jug_solver():
    visited = set()
    queue = deque()

    # Each element: (jug1, jug2, path)
    queue.append((0, 0, []))

    while queue:
        x, y, path = queue.popleft()

        # If already visited
        if (x, y) in visited:
            continue

        visited.add((x, y))
        path = path + [(x, y)]

        # Check goal
        if x == GOAL or y == GOAL:
            return path

        # Generate all possible next states
        next_states = []

        # Fill Jug1
        next_states.append((JUG1, y))

        # Fill Jug2
        next_states.append((x, JUG2))

        # Empty Jug1
        next_states.append((0, y))

        # Empty Jug2
        next_states.append((x, 0))

        # Pour Jug1 -> Jug2
        transfer = min(x, JUG2 - y)
        next_states.append((x - transfer, y + transfer))

        # Pour Jug2 -> Jug1
        transfer = min(y, JUG1 - x)
        next_states.append((x + transfer, y - transfer))

        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path))

    return None

# -------- MAIN --------

solution = water_jug_solver()

if solution:
    print("Steps to reach the goal:\n")
    for step in solution:
        print(step)
else:
    print("No solution found")
