# 알고리즘 - bfs 
from collections import deque
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")
input = sys.stdin.readline

row, col = map(int, input().split())
board = []
visited = [[False]*(col) for _ in range(row)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(row):
  tmp = list(map(int, input().split()))
  board.append(tmp)
  if 2 in tmp:
    idx = tmp.index(2)
    start_x, start_y = i, idx
    board[start_x][start_y] = 0
# print(board) # 이거 출력한 채로 제출해서 WA뜬거 맞왜틀함..

def bfs(i, j):
  dq = deque()
  dq.append((i, j))
  visited[i][j] = True
  while dq:
    x, y = dq.popleft()
    for a in range(4):
      x_ = x + dx[a]
      y_ = y + dy[a]
      if 0 <= x_ < row and 0 <= y_ < col and not visited[x_][y_] and board[x_][y_] == 1:
        dq.append((x_, y_))
        board[x_][y_] = board[x][y] + 1
        visited[x_][y_] = True
  
bfs(start_x, start_y)
for i in range(row):
  for j in range(col):
    if board[i][j] == 1 and not visited[i][j]:
      board[i][j] = -1

for i in range(row):
  print(*board[i])