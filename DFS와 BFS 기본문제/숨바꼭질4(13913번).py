# 두번째 코드 -> path 리스트를 하나만 사용해서 지나온 직전 노드를(번호) 저장
from collections import deque
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\DFS와 BFS 기본문제\\input.txt"
sys.stdin = open(filePath, "rt")

n, k = map(int, input().split())

def bfs():
  dq = deque()
  times = [-1]*100001
  pathList = [-1]*(100001)
  times[n] = 0
  dq.append(n)
  while dq:
    now = dq.popleft()
    if now == k:
      path = [now]
      while now != n:
        path.append(pathList[now])
        now = pathList[now]
      # path에는 마지막 도착지점(k)부터 시작해서 root노드인 n번노드까지, 역순으로 지나온 경로가 저장되어 있으므로 이를 뒤집어서 출력해야 한다.
      path.reverse()
      return times[k], path
    
    for x in [now-1, now+1, now*2]:
      if 0 <= x < 100001 and times[x] == -1:
        times[x] = times[now] + 1 
        pathList[x] = now # pathList의 현재 노드(x)에는 부모노드(now)를 저장한다. 
        dq.append(x)

time, path = bfs()
print(time)
print(*path)


'''
# 첫번째 풀이 -> 시간초과
  why? => bfs에서 dq에 들어가는 path 리스트를 매번 새로 만들기 때문에 최악의 경우, 입력으로 100000 0 이 들어온다면 마지막에 정답에 해당하는 path리스트의 원소갯수는 1000001개가 된다.
          즉, 원소에 0~100000 까지의 숫자가 모두 들어가게 된다.(100000에서 시작해서 1씩 감소해서 0으로 도착하는 방법밖에 없으므로)
          이때, 이 리스트를 얻기 위해서는 원소가 1개인 리스트부터 100001개인 리스트까지 전부 만들어가면서 반복문을 수행하게 된다.
          새로운 리스트를 만드는데 필요한 연산은 원소의 갯수와 같으므로(O(n)) 이로인해 시간초과가 발생하는 것이라 생각된다.

from collections import deque
n, k = map(int, input().split())

def bfs():
  dq = deque()
  times = [-1]*100001
  times[n] = 0
  dq.append([n, [n]])
  while dq:
    now, path = dq.popleft()
    if now == k:
      return times[now], path
    
    for x in [now-1, now+1, now*2]:
      if 0 <= x < 100001 and times[x] == -1:
        times[x] = times[now] + 1 
        tmp = path + [x]
        dq.append([x, tmp])

time, path = bfs()
print(time)
print(*path)
'''