# 알고리즘 - bfs
# 두번째 코드 -> 메모리 절약된 코드 
#               굳이 days 배열을 만들 필요 없이 level만 구해도 된다.(bfs는 동일한 level인 원소는 같이 탐색하므로)
#               그리고 탐색한 후 tomato[x_][y_] = 1을 해줌으로써, if 조건문인 tomato[x_][y_] == 0에서 이미 탈락하기 때문에 visited 배열도 따로 만들어 줄 필요 없다. 
#               원본 배열인 tomato 배열의 요소값들이 변경되어도 상관없는 문제이므로 그냥 이미 들렸다는 표시로 tomato[x_][y_] = 1을 해주면 방문처리가 된 것이나 마찬가지다.
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
    x, y, d = dq.popleft()
    for a in range(4):
      x_ = x + dx[a]
      y_ = y + dy[a]
      if 0 <= x_ < row and 0 <= y_ < col and  tomato[x_][y_] == 0:
        tomato[x_][y_] = 1
        dq.append((x_, y_, d+1))

  if any(0 in tomato[i] for i in range(row)):
    return -1  
  else:
    return d

dq = deque()
for i in range(row):
  for j in range(col):
    if tomato[i][j] == 1:
      dq.append((i, j, 0)) # (x좌표, y좌표, level) -> 맨 처음 dq에 들어가는 토마토의 level은 0

print(bfs())


''' 첫번째 코드 -> correct
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

'''