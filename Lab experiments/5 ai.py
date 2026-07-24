from collections import deque

# Check if state is valid
def is_valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m > 0 and m < c:
        return False
    if (3-m) > 0 and (3-m) < (3-c):
        return False
    return True

# BFS Solver
def solve():
    start = (3, 3, 0)
    goal = (0, 0, 1)

    queue = deque()
    visited = set()

    queue.append((start, []))

    while queue:
        (m, c, b), path = queue.popleft()

        if (m, c, b) == goal:
            path = path + [(m, c, b)]
            return path

        if (m, c, b) in visited:
            continue

        visited.add((m, c, b))
        path = path + [(m, c, b)]

        # Possible moves
        moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

        for dm, dc in moves:
            if b == 0:  # boat on left
                nm, nc, nb = m - dm, c - dc, 1
            else:       # boat on right
                nm, nc, nb = m + dm, c + dc, 0

            if is_valid(nm, nc):
                queue.append(((nm, nc, nb), path))

    return None

# -------- MAIN --------
solution = solve()

print("Steps (M_left, C_left, Boat_side):\n")
for step in solution:
    print(step)
