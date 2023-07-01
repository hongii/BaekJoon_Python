# 알고리즘 - dfs/bfs
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

row, col = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
board = []
cnt = 0
for i in range(row):
  tmp = list(input().rstrip())
  board.append(tmp)
  if "I" in tmp:
    j = tmp.index("I")
    start = (i, j)

def dfs(i, j):
  global cnt
  for a in range(4):
    x = i + dx[a]
    y = j + dy[a]
    if 0 <= x < row and 0 <= y < col and (board[x][y] == "O" or board[x][y] == "P"):
      if board[x][y] == "P":
        cnt += 1
      board[x][y] = "X"
      dfs(x, y)

dfs(start[0], start[1])
print(cnt if cnt > 0 else "TT")


