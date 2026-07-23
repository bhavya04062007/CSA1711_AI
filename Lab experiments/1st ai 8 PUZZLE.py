from collections import deque

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 4, 2,
        3, 0, 5,
        6, 7, 8)

moves = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs(start, goal):
    q = deque([(start, [])])
    visited = set()

    while q:
        state, path = q.popleft()

        if state == goal: 
            return path + [state]

        if state in visited:
            continue

        visited.add(state)

        zero = state.index(0)
        r, c = divmod(zero, 3)

        for dr, dc in moves:
            nr, nc = r + dr, c + dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                new = list(state)
                ni = nr * 3 + nc

                new[zero], new[ni] = new[ni], new[zero]

                q.append((tuple(new), path + [state]))

    return None

solution = bfs(start, goal)

if solution:
    print("Solution Found!\n")

    for step in solution:
        for i in range(0,9,3):
            print(step[i:i+3])
        print()
else:
    print("No Solution")
