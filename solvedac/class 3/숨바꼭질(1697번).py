from collections import deque
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")

n, k = map(int, input().split())
times = [float('inf')] * 200001
times[n] = 0
dq = deque()
dq.append(n) #(시작번호, 걸린시간)
while dq:
  now = dq.popleft()
  if now == k:
    print(times[k])
    break

  arr = [now-1, now+1, now*2]
  for x in arr:
    if 0 <= x <= 200000 and times[x] == float('inf'):
      times[x] = times[now] + 1
      dq.append(x)
