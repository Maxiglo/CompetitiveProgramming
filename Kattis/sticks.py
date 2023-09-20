from collections import defaultdict, deque

def topological_sort(graph):
    indegree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    queue = deque([node for node in graph if indegree[node] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return result if len(result) == len(graph) else []

def pick_up_sticks(n, m, relationships):
    graph = defaultdict(list)

    for a, b in relationships:
        graph[a].append(b)
    
    # Initialize indegree for all sticks
    for i in range(1, n + 1):
        if i not in graph:
            graph[i] = []

    order = topological_sort(graph)

    if not order:
        return "IMPOSSIBLE"
    else:
        return order


n, m = map(int, input().split())
relationships = [tuple(map(int, input().split())) for _ in range(m)]

result = pick_up_sticks(n, m, relationships)

if result == "IMPOSSIBLE":
    print(result)
else:
    for stick in result:
        print(stick)
