# Prim's Algorithm without INF and without any libraries

# Step 1: Input
n = int(input("Enter number of vertices: "))
print("Enter the adjacency matrix (use 0 if no edge):")

graph = []
for i in range(n):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    graph.append(row)

# Step 2: Initialize
selected = [False] * n
selected[0] = True  # Start from first vertex
edges = 0

print("\nMinimum Spanning Tree:")
print("Edge \tWeight")

# Step 3: Loop until n-1 edges are selected
while edges < n - 1:
    min_weight = 999999
    u = -1
    v = -1

    for i in range(n):
        if selected[i]:
            for j in range(n):
                if not selected[j] and graph[i][j] != 0:
                    if graph[i][j] < min_weight:
                        min_weight = graph[i][j]
                        u = i
                        v = j

    if u != -1 and v != -1:
        print(f"{u} - {v} \t{graph[u][v]}")
        selected[v] = True
        edges += 1