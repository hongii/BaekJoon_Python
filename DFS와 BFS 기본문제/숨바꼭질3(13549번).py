# 두번째 코드 -> 가중치가 서로 다른 간선일때 최단거리(최소시간) 구하는 문제 : 다익스트라 알고리즘 이용
import heapq
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\DFS와 BFS 기본문제\\input.txt"
sys.stdin = open(filePath, "rt")

n, k = map(int, input().split())

def Dijkstra(n, k):
  hq = []
  heapq.heappush(hq, (0, n))
  times = [10e9]*100001
  times[n] = 0
  while hq:
    time, now = heapq.heappop(hq)
    if time > times[now]:
      continue
    
    if now == k:
      break

    else:
      for x in [now-1, now+1, now*2]: 
        if 0 <= x < 100001:
          if x == now*2 and times[x] > time:
            times[x] = time
            heapq.heappush(hq, (times[x], x))
          elif x != now*2 and times[x] > time+1:
            times[x] = time + 1
            heapq.heappush(hq, (times[x], x))
  print(times[k])

Dijkstra(n, k)


'''
# 여러번 수정과정 거친 첫번째 코드 -> BFS
from collections import deque
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\DFS와 BFS 기본문제\\input.txt"
sys.stdin = open(filePath, "rt")
n, k = map(int, input().split())
dq = deque()
visited = [False]*100001
dq.append((n, 0))
minTime = 10e9
while dq:
  print(deque)
  now, time = dq.popleft()
  visited[now] = True
  if now == k and time <= minTime:
    minTime = time
    break
  if time > minTime:
    continue

  else:
    for x in [now*2,now-1, now+1]: # 여기서 주의! 순간이동 하는 경우(now*2)의 가중치가 0이므로(0초) 가장 우선순위가 높다. now*2부터 비교를 해줘야 한다. 이게 헷갈리면 다익스트라로 구현하기 
      if 0 <= x < 100001 and not visited[x]:
        if x == now*2:
          dq.append((x, time))
        else:
          dq.append((x, time+1))
print(minTime)

# 맨 처음에 위의 풀이에서 for x in [now-1, now+1, now*2]: 순으로 비교를 해서 계속 WA가 떴음
'''