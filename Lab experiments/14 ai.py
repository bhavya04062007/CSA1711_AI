def minimax(depth, node, is_max, values):
    # Leaf nodes at depth 2
    if depth == 2:
        return values[node]

    if is_max:
        return max(
            minimax(depth + 1, node * 2, False, values),
            minimax(depth + 1, node * 2 + 1, False, values)
        )
    else:
        return min(
            minimax(depth + 1, node * 2, True, values),
            minimax(depth + 1, node * 2 + 1, True, values)
        )


values = [3, 5, 2, 9]
print("Optimal value:", minimax(0, 0, True, values))
