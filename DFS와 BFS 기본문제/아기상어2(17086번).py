from collections import deque
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\DFS와 BFS 기본문제\\input.txt"
sys.stdin = open(filePath, "rt")

row, col = map(int, input().split())
board = []
for _ in range(row):
  board.append(list(map(int, input().split())))

save = [[51]*col for _ in range(row)]
def bfs(i, j):
  dq = deque()
  visited = [[False]*col for _ in range(row)]
  dx = [-1, -1, 0, 1, 1, 1, 0, -1] # 8방향 (12시->1시->3시->5시->6시->7시->9시->11시)
  dy = [0, 1, 1, 1, 0, -1, -1, -1]
  dq.append((i, j))
  save[i][j] = 0

  while dq:
    x, y = dq.popleft()
    for a in range(8):
      x_ = x + dx[a]
      y_ = y + dy[a]
      if 0 <= x_ < row and 0 <= y_ < col and not visited[x_][y_] and board[x_][y_] != 1:
        save[x_][y_] = min(save[x_][y_], save[x][y] + 1)
        visited[x_][y_] = True
        dq.append((x_, y_))


for i in range(row):
  for j in range(col):
    if board[i][j] == 1:
      bfs(i, j)
print(max(map(max, save)))