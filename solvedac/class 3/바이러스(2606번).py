# 알고리즘 - bfs/dfs
from collections import deque
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")

computers = int(input())
m = int(input())
network = [[] for _ in range(computers+1)]
for _ in range(m):
  a, b = map(int, input().split())
  network[a].append(b)
  network[b].append(a)

cnt = 0
dq = deque()
visited = [False] * (computers+1)
dq.append(1)
visited[1] = True
while dq:
  now = dq.popleft()
  for x in network[now]:
    if not visited[x]:
      visited[x] = True
      dq.append(x)
      cnt += 1
print(cnt)