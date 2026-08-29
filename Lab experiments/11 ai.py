def color_map(graph, colors, result={}):
    if len(result) == len(graph):
        return result

    state = next(s for s in graph if s not in result)

    for color in colors:
        if all(result.get(n) != color for n in graph[state]):
            result[state] = color
            if color_map(graph, colors, result):
                return result
            result.pop(state)
    return None


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}

colors = ['Red', 'Green', 'Blue']

print(color_map(graph, colors))
