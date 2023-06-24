# 알고리즘 - dfs/bfs
# 두번째 풀이 -> correct, bfs
from collections import deque
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
  v1, v2 = map(int, input().split())
  graph[v1].append(v2)
  graph[v2].append(v1)

def bfs(x):
  dq = deque()
  dq.append(x)
  visited[x] = True
  while dq:
    v = dq.popleft()
    for u in graph[v]:
      if not visited[u]:
        visited[u] = True
        dq.append(u)

group = 0
visited = [False] * (V+1)
for i in range(1, V+1):
  # 고립된 노드인 경우, 단독 그룹 형성
  if not graph[i]:
    group += 1
    visited[i] = True
  elif not visited[i]:
    bfs(i)
    group += 1
print(group)




''' 첫 번째 풀이 -> correct, 사이클 판별 응용(feat. 크루스칼 알고리즘)
import sys
input = sys.stdin.readline
V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
parent = [i for i in range(V+1)]
for _ in range(E):
  v1, v2 = map(int, input().split())
  graph[v1].append(v2)
  graph[v2].append(v1)


def find_parent(x):
  if x != parent[x]:
    parent[x] = find_parent(parent[x])
  return parent[x]

def union(a, b):
  root_a = find_parent(a)
  root_b = find_parent(b)
  if root_a > root_b:
    parent[root_a] = root_b
  else: 
    parent[root_b] = root_a

group = 0
for i in range(1, V+1):
  for x in graph[i]:
    if find_parent(x) != find_parent(i):
      union(x, i)

print(len(set(parent[1:])))

'''

