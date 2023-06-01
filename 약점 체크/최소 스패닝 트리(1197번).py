import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\약점 체크\\input.txt"
sys.stdin = open(filePath, "rt")
v, e = map(int, input().split())
parent = [i for i in range(v+1)]
edges = []
for _ in range(e):
    a, b, w = map(int, input().split())
    edges.append((w, a, b))
edges.sort() # 가중치순으로 오름차순 정렬

def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
    return parent[a]

def union(a, b):
    a_root = find_parent(a)
    b_root = find_parent(b)
    if a_root < b_root:
        parent[b_root] = a_root
    else:
        parent[a_root] = b_root

res = 0
for edge in edges:
    w, a, b = edge
    # 사이클이 발생하지 않은 경우에는 같은 집합으로 포함시킴
    if find_parent(a) != find_parent(b):
        union(a, b)
        res += w
print(res)