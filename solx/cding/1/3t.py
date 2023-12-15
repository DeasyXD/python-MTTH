graph = {}
edges = int(input())
for _ in range(edges):
    start, end, distance = map(int, input().split())
    if start not in graph:
        graph[start] = []
    graph[start].append((end, distance))
print(graph)
print(graph[1][0][0])