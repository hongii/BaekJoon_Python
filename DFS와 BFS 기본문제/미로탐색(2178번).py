from collections import deque
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\DFS와 BFS 기본문제\\input.txt"
sys.stdin = open(filePath, "rt")

n, m = map(int, input().split())
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

def bfs(i, j):
  dx = [-1, 0, 1, 0]
  dy = [0, 1, 0, -1]
  dq = deque()
  distance = [[0]*m for _ in range(n)]
  visited = [[False]*m for _ in range(n)]
  
  dq.append((i, j))
  visited[i][j] = True
  distance[i][j] = 1 # 시작위치도 포함해서 센다고 문제 조건에 주어짐

  while dq:
    x, y = dq.popleft()
    if x == n-1 and y == m-1:
      return distance[x][y]
    for k in range(4):
      x_ = x + dx[k]
      y_ = y + dy[k]
      if 0 <= x_ < n and 0 <= y_ < m and not visited[x_][y_] and graph[x_][y_] == 1:
        visited[x_][y_] = True
        distance[x_][y_] = distance[x][y] + 1
        dq.append((x_, y_))

print(bfs(0, 0))