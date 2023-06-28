from collections import deque
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")
input = sys.stdin.readline

n = int(input())
RGB = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for _ in range(n):
  RGB.append(list(input().rstrip()))

def bfs(i, j, color, check):
  dq = deque()
  visited[i][j] = True
  dq.append((i, j))
  while dq:
    x, y = dq.popleft()
    for a in range(4):
      x_ = x + dx[a]
      y_ = y + dy[a]
      if check == "RGB" or (check == "RB" and color == "B"): # 정상인 경우 OR 적록색약이면서 color가 "B"인 경우
        if 0 <= x_ < n and 0 <= y_ < n and not visited[x_][y_] and RGB[x_][y_] == color:
          visited[x_][y_] = True
          dq.append((x_, y_))
      
      elif check == "RB": # 적록색약이면서 color가 "R" 또는 "G"인 경우
        if 0 <= x_ < n and 0 <= y_ < n and RGB[x_][y_] in ["R", "G"] and not visited[x_][y_] and (RGB[x_][y_] == "R" or RGB[x_][y_] == "G"):
          visited[x_][y_] = True
          dq.append((x_, y_))

visited = [[False]*n for _ in range(n)]
RGBcnt = 0
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      RGBcnt += 1
      bfs(i, j, RGB[i][j], "RGB")

visited = [[False]*n for _ in range(n)]
RBcnt = 0
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      RBcnt += 1
      bfs(i, j, RGB[i][j], "RB")
print(RGBcnt, RBcnt)