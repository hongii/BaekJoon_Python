import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")
sys.setrecursionlimit(10**6)

T = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(i, j):
  board[i][j] = 0
  for a in range(4):
    x = i + dx[a]
    y = j + dy[a]
    if 0 <= x < row and 0 <= y < col and board[x][y] == 1:
      board[i][j] = 0
      dfs(x, y)

while T:
  T -= 1
  col, row, k = map(int, input().split())
  board = [[0]*col for _ in range(row)]
  for _ in range(k):
    y, x = map(int, input().split())
    board[x][y] = 1

  cnt = 0
  for i in range(row):
    for j in range(col):
      if board[i][j] == 1:
        dfs(i, j)
        cnt += 1
  print(cnt)