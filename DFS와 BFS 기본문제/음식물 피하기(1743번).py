import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\DFS와 BFS 기본문제\\input.txt"
sys.stdin = open(filePath, "rt")
sys.setrecursionlimit(10**6)

row, col, k = map(int, input().split())
graph = [[0]*col for _ in range(row)]
for i in range(k):
  x, y = map(int, input().split())
  graph[x-1][y-1] = 1

def dfs(i, j, res):
  dx = [-1, 0, 1, 0]
  dy = [0, 1, 0, -1]
  graph[i][j] = 0
  for a in range(4):
    x = i + dx[a]
    y = j + dy[a]
    if 0 <= x < row and 0 <= y < col and graph[x][y] == 1:
      res = dfs(x, y, res+1)
  return res

maxCnt = 0
for i in range(row):
  for j in range(col):
    if graph[i][j] == 1:
      cnt = dfs(i, j, 1)
      if maxCnt < cnt:
        maxCnt = cnt
print(maxCnt)



