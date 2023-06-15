from collections import deque
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\최근 빈출 유형 문제\\input.txt"
sys.stdin = open(filePath, "rt")

T = int(input())
while T:
  K, M, P = map(int, input().split())
  inDegree = [[0, 0, 0] for _ in range(M+1)] # [진입차수, strahler 순서, strahler 순서가 동일한 진입 간선의 갯수]
  graph = [[] for _ in range(M+1)]
  dq = deque()
  for _ in range(P):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b][0] += 1

  for i in range(1, M+1):
    if inDegree[i][0] == 0:
      inDegree[i][1] = 1
      dq.append(i)
  
  while dq:
    now = dq.popleft()

    for u in graph[now]:
      inDegree[u][0] -= 1
      if inDegree[u][1] == inDegree[now][1]:
        inDegree[u][2] += 1
      elif inDegree[u][1] < inDegree[now][1]:
        inDegree[u][1] = inDegree[now][1]
        inDegree[u][2] = 1
      
      if inDegree[u][0] == 0:
        if inDegree[u][2] > 1:
          inDegree[u][1] += 1
        dq.append(u)
  print(T, inDegree[M][1])
  T -= 1


'''T = int(input())
while T:
  K, M, P = map(int, input().split())
  inDegree = [0] * (M+1) 
  graph = [[] for _ in range(M+1)]
  dq = deque()
  strahler = [(0, 0)]*(M+1) # (strahler 순서, strahler 순서가 동일한 진입 간선의 갯수)
  for _ in range(P):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1

  for i in range(1, M+1):
    if inDegree[i] == 0:
      strahler[i] = (1, 0)
      dq.append(i)
  
  while dq:
    print(dq)
    now = dq.popleft()

    for u in graph[now]:
      inDegree[u] -= 1
      print(u, inDegree)
      cnt = strahler[u][1]
      if strahler[u][0] == strahler[now][0]:
        cnt += 1
      elif strahler[u][0] < strahler[now][0]:
        cnt = 1
      strahler[u] = (strahler[now][0], cnt)
      
      if inDegree[u] == 0:
        if strahler[u][1] > 1:
          strahler[u] = (strahler[u][0] + 1, 0)
        dq.append(u)
      print(strahler)
  print(T, max(strahler, key=lambda x: x[0])[0])
  T -= 1'''


'''첫번째 코드 -> WA, 예제는 맞는데 테케 12%에서 WA
T = int(input())
while T:
  K, M, P = map(int, input().split())
  inDegree = [0] * (M+1)
  graph = [[] for _ in range(M+1)]
  dq = deque()
  strahler = [(0, 0)]*(M+1) # (strahler 순서, strahler 순서가 동일한 진입 간선의 갯수)
  for _ in range(P):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1

  print(graph, inDegree)
  for i in range(1, M+1):
    if inDegree[i] == 0:
      strahler[i] = (1, 0)
      dq.append((i, 1)) # (노드 번호, Strahler 순서)

  while dq:
    print(dq)
    now, s = dq.popleft()
    if strahler[now][0] > s:
      continue
    print(now, s, strahler[now], strahler)
    for u in graph[now]:
      cnt = strahler[u][1]
      if strahler[u][0] == s:
        if strahler[u][1] == 1:
          s += 1
          cnt = 0
        else:
          cnt += 1
      elif strahler[u][0] < s:
        cnt = 1
      elif strahler[u][0] > s:
        continue
      strahler[u] = (s, cnt)
      dq.append((u, s))
  print(T, max(strahler)[0])
  T -= 1
'''

