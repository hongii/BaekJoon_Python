import sys
from collections import deque
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")
input = sys.stdin.readline

n, m = map(int, input().split())
ladder = {}
for _ in range(n):
  a, b = map(int, input().split())
  ladder[a] =  b

snake = {}
for _ in range(m):
  a, b = map(int, input().split())
  snake[a] = b

visited = [False]*(101)
visited[1] = True
dq = deque()
dq.append((1, 0))
while dq:
  site, cnt = dq.popleft()

  if site == 100: # 도착지점인 100위치에 도달했으면 cnt 출력 후 종료
    print(cnt)
    break

  for i in range(1, 7): # 주사위 1~6 까지 돌리면서 이동
    if site+i <= 100 and not visited[site+i]: # 아직 해당 위치에 방문하지 않았다면,
      next = site+i
      if site+i in ladder.keys():
        next = ladder[site+i]
      if site+i in snake.keys():
        next = snake[site+i]
      
      visited[next] = True
      dq.append((next, cnt+1))