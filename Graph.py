from collections import defaultdict, deque

graph = defaultdict(set)
nodes = set()
with open('data-assgn-7.txt', 'r') as file :
    for line in file :
        u, v = map(int, line.strip().split())
        graph[u].add(v)
        graph[v].add(u)
        nodes.update([u, v])

def bestFirstSearch(start) : #apply BFS and store all bridge edges and all visited nodes
    parent = {start: None}
    level = {start: 0}
    q = deque([start])
    Edges = set()
    nonEdges = []
    visitedNodes = {start}

    while q: 
        u = q.popleft()
        for v in graph[u]:
            if v not in parent: 
                parent[v] = u
                level[v] = level[u]+1
                q.append(v)
                Edges.add((min(u, v), max(u, v)))
                visitedNodes.add(v)
            elif parent[u] != v:
                nonEdges.append((u, v))
                
    bridges = set(Edges)
    for u, v in nonEdges:
        while level[u] > level[v] :
            e = (min(u, parent[u]), max(u, parent[u]))
            bridges.discard(e)
            u = parent[u]
        while level[u] < level[v] :
            e = (min(v, parent[v]), max(v, parent[v]))
            bridges.discard(e)
            v = parent[v]
        while u != v :
            e = (min(u, parent[u]), max(u, parent[u]))
            bridges.discard(e)
            u = parent[u]
            e = (min(v, parent[v]), max(v, parent[v]))
            bridges.discard(e)
            v = parent[v]

    return bridges, visitedNodes


def findBridges(): # BFS on each component, returns all bottleneck bridges
    bridges = set()
    seen = set()
    for node in nodes:
        if node not in seen : 
            compBridge, compNodes = bestFirstSearch(node)
            bridges.update(compBridge)
            seen.update(compNodes)
    return sorted(bridges)

import time
start = time.time()
bottlenecks = findBridges()
end = time.time()
print("Time taken:", end - start, "seconds")
print("Number of bottlenecks: ", len(bottlenecks))
print("Bottleneck Edges: ")
for u, v in bottlenecks:
    print(u, ",", v)