# 알고리즘 - bfs
from collections import deque
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")

col, row = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
tomato = []
for i in range(row):
  tomato.append(list(map(int, input().split())))

def bfs():
  while dq:
    x, y = dq.popleft()
    for a in range(4):
      x_ = x + dx[a]
      y_ = y + dy[a]
      if 0 <= x_ < row and 0 <= y_ < col and  tomato[x_][y_] == 0 and not visited[x_][y_]:
        tomato[x_][y_] = 1
        days[x_][y_] = days[x][y] + 1
        visited[x_][y_] = True
        dq.append((x_, y_))

  if all(0 not in tomato[i] for i in range(row)):
    return max(map(max, days)) # 2차원 리스트에서 최댓값 구하는 방법 -> map함수 이용
  else:
    return -1


dq = deque()
days = [[0 for _ in range(col)] for _ in range(row)]
visited = [[False for _ in range(col)] for _ in range(row)]
for i in range(row):
  for j in range(col):
    if tomato[i][j] == 1:
      visited[i][j] = True
      dq.append((i, j))

print(bfs())