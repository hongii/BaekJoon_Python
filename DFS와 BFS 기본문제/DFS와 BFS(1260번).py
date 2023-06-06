from collections import deque
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\DFS와 BFS 기본문제\\input.txt"
sys.stdin = open(filePath, "rt")
n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    v, u = map(int, input().split())
    graph[v].append(u)
    graph[u].append(v)

for i in range(1, n+1):
    graph[i].sort()

visited_dfs = [False]*(n+1)
def dfs(x):
    visited_dfs[x] = True
    print(x, end=" ")
    for v in graph[x]:
        if not visited_dfs[v]:
            dfs(v)

def bfs(x):
    dq = deque()
    visited_bfs = [False]*(n+1)
    dq.append(x)
    visited_bfs[x] = True
    while dq:
        now = dq.popleft()
        print(now, end=" ")
        for v in graph[now]:
            if not visited_bfs[v]:
                visited_bfs[v] = True
                dq.append(v)

dfs(start)
print()
bfs(start)