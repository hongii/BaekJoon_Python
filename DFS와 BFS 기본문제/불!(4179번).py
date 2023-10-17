# bfs
# 이 문제에서는 fire의 bfs를 먼저 돌려서 fire의 전파시간을 먼저 구하고 난 후, 
# 지훈이의 bfs를 돌리면서 지훈이가 먼저 도달 가능한 지점이라면(time_fire[x][y] > time[x][y]) 지훈이를 이동시키도록 구현해도 됨
# 주의할 것 => BOJ 18809번의 경우, 이렇게 풀면 안됨(개별로 bfs 돌리면 안되고 한번에 돌려야함)
from collections import deque
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\DFS와 BFS 기본문제\\input.txt"
sys.stdin = open(filePath, "rt")

input = sys.stdin.readline
row, col = map(int, input().split())
board = []
jihoon, fire = [], []
for i in range(row):
  tmp = list(input().rstrip())
  board.append(tmp)
  if "J" in tmp:
    j = tmp.index("J")
    jihoon.append((i, j))
  if "F" in tmp: # 처음에 틀린이유 1) "F"가 한개라는 말 없다..주의하자
    j = tmp.index("F")
    fire.append((i, j))
# print(board, jihoon, fire)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def bfs_fire(fire):
  dq = deque()
  time = [[float('inf')]*col for _ in range(row)]
  for site in fire:
    i, j = site[0], site[1]
    time[i][j] = 0
    dq.append((i, j))

  while dq:
    x, y = dq.popleft()
    for a in range(4):
      x_ = x + dx[a]
      y_ = y + dy[a]
      if 0 <= x_ < row and 0 <= y_ < col and time[x_][y_] > time[x][y] + 1 and board[x_][y_] != "#":
        time[x_][y_] = time[x][y] + 1
        dq.append((x_, y_))
  return time

def bfs_jihoon(i, j, time_fire):
  dq = deque()
  time = [[float('inf')]*col for _ in range(row)]
  time[i][j] = 0
  dq.append((i, j))
  while dq:
    x, y = dq.popleft()
    if x == row-1 or y == col-1 or x == 0 or y == 0: # 처음에 틀린이유 2) x == 0 과 y == 0인 조건을 안넣어줌..
      return time[x][y] + 1
    
    for a in range(4):
      x_ = x + dx[a]
      y_ = y + dy[a]
      if 0 <= x_ < row and 0 <= y_ < col and time[x_][y_] > time[x][y] + 1 and time_fire[x_][y_] > time[x][y] + 1 and board[x_][y_] == ".":
        time[x_][y_] = time[x][y] + 1
        dq.append((x_, y_))
  
  return float('inf')

time_fire = bfs_fire(fire)
res = bfs_jihoon(jihoon[0][0], jihoon[0][1], time_fire)
print(res if res != float('inf') else "IMPOSSIBLE")