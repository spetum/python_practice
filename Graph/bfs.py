
## https://github.com/minsuk-heo/problemsolving/blob/master/graph/dfs.py
# vertex를 저장
vertexLists = ['0', '1', '2', '3', '4', '5', '6']
# edge들의 incident list임 ; edge들이 어느 vertex를 연결해주는지 표시
edgeLists = [(0,1), (0,2), (1,0), (1,3),
            (2,0), (2,4), (2,5), (3,1),
            (4,2), (4,6), (5,2), (6,4)]
graphs = (vertexLists, edgeLists)

def bfs(graph, start):
    vertexList, edgeList = graph
    visitedList = []
    queue = [start]
    adjacencyList = [[] for vertex in vertexList]

    # fill adjacencyList from graph
    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    # bfs
    while queue:
        current = queue.pop()
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedList:
                queue.insert(0,neighbor)
        visitedList.append(current)
    return visitedList

print(bfs(graphs, 0))