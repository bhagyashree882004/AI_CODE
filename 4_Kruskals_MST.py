class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu != pv:
            self.parent[pu] = pv
            return True
        return False


def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    dsu = DisjointSet(n)
    mst = []
    total_cost = 0

    for u, v, weight in edges:
        if dsu.union(u, v):
            mst.append((u, v, weight))
            total_cost += weight

    return mst, total_cost


# === User Input ===
print("Enter number of vertices and edges:")
n = int(input("Number of vertices: "))
e = int(input("Number of edges: "))

edges = []
print("\nEnter each edge in the format: u v weight")
for _ in range(e):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

# === Run Kruskal ===
mst, cost = kruskal(n, edges)

print("\nEdges in the Minimum Spanning Tree:")
for u, v, w in mst:
    print(f"{u} - {v}: {w}")

print(f"Total cost of MST: {cost}")
