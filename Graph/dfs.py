
# https://github.com/minsuk-heo/problemsolving/blob/master/graph/dfs.py
vertexLists = ['0', '1', '2', '3', '4', '5', '6']
#edgeLists = [(0,1), (1,3), (0,2), (2,4), (4,6), (2,5)]
edgeLists = [(0,1), (0,2), (1,0), (1,3),
            (2,0), (2,4), (2,5), (3,1),
            (4,2), (4,6), (5,2), (6,4)]
graphs = (vertexLists, edgeLists)

def dfs(graph, start):
    vertexList, edgeList = graph
    visitedVertex = []
    stack = [start]
    adjacencyList = [[] for vertex in vertexList]

    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    while stack:
        current = stack.pop()
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedVertex:
                stack.append(neighbor)
        visitedVertex.append(current)
    return visitedVertex

print(dfs(graphs, 0))