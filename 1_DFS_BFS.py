def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

def bfs(visited, graph, node):
    queue = []  # List वापरून queue तयार
    visited.add(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)  # Queue मधून पहिला घटक काढतो (FIFO)
        print(s, end=" ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

def main():
    visited1 = set()  # DFS साठी visited नोड्स
    visited2 = set()  # BFS साठी visited नोड्स
    graph = dict()    # रिकामं graph तयार

    n = int(input("Enter number of nodes: "))  # नोड्सची संख्या विचारतो
    
    # प्रत्येक नोडसाठी edges घ्या
    for i in range(1, n+1):
        edges = int(input(f"Enter number of edges for node {i}: "))
        if i not in graph:
            graph[i] = []
        for j in range(1, edges+1):
            node = int(input(f"Enter edge {j} for node {i}: "))
            graph[i].append(node)
            if node not in graph:
                graph[node] = []
            graph[node].append(i)  # Undirected Graph असल्यामुळे दोन्ही बाजूंनी जोड

    print("\nThe following is DFS Traversal:")
    dfs(visited1, graph, 1)  # DFS सुरू नोड 1 पासून

    print("\n\nThe following is BFS Traversal:")
    bfs(visited2, graph, 1)  # BFS सुरू नोड 1 पासून

if __name__ == "__main__":
    main()
