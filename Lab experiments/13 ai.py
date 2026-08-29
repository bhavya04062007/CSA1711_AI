def alphabeta(d, n, a, b, maxp, v):
    if d == 2:
        return v[n]

    if maxp:
        for i in range(2):
            a = max(a, alphabeta(d+1, n*2+i, a, b, False, v))
            if a >= b:
                break
        return a
    else:
        for i in range(2):
            b = min(b, alphabeta(d+1, n*2+i, a, b, True, v))
            if b <= a:
                break
        return b


values = [8, 4, 6, 2]
print("Optimal value:", alphabeta(0, 0, -1000, 1000, True, values))
