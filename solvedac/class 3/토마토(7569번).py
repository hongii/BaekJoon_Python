# 토마토(7576번)에서 좀 더 업그레이드 된 문제? 3차원 배열
# 알고리즘 - bfs
from collections import deque
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")

input = sys.stdin.readline
col, row, height = map(int, input().split())
dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

tomato = [[] for _ in range(height)]
for h in range(height):
  for i in range(row):
    tomato[h].append(list(map(int, input().split())))

dq = deque()
for h in range(height):
  for i in range(row):
    for j in range(col):
      if tomato[h][i][j] == 1:
        dq.append((h, i, j, 0)) # (z좌표, x좌표, y좌표, 깊이(=level))

def bfs():
  days = 0
  while dq:
    z, x, y, d = dq.popleft()
    days = d
    for i in range(6):
      x_ = x + dx[i]
      y_ = y + dy[i]
      z_ = z + dz[i]
      if 0 <= x_ < row and 0 <= y_ < col and 0 <= z_ < height and tomato[z_][x_][y_] == 0:
        tomato[z_][x_][y_] = 1
        dq.append((z_, x_, y_, d+1))

  if any(0 in tomato[k][i] for k in range(height) for i in range(row)):
    return -1
  else:
    return days


print(bfs())