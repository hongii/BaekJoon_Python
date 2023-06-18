# 알고리즘 - 다이나믹 프로그래밍 
# cf) 나는 bfs로 품
from collections import deque
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")

# 첫번째 풀이 -> correct, bfs로 폴었음
n = int(input())
dq = deque()
dq.append((n, 0)) # (num, depth(=level))
distance = [10e6]*(n+1)
distance[n] = 0
while dq:
  print(dq)
  num, d = dq.popleft()
  if num == 1:
    print(d)
    break
  
  if num % 3 == 0 and distance[num//3] > d+1:
    dq.append((num//3, d+1))
    distance[num//3] = d+1
  if num % 2 == 0 and distance[num//2] > d+1:
    dq.append((num//2, d+1))
    distance[num//2] = d+1
  if num > 1 and distance[num-1] > d+1:
    dq.append((num-1, d+1))
    distance[num-1] = d+1


'''
# 두번째 풀이 -> dp이용
n = int(input())
dp = [0]*(n+1) # 각 index에 해당하는 숫자를 만들 수 있는 최소 연산 횟수가 담긴다.
for i in range(2, n+1):
  # i를 만드는 방법 중 하나는 직전 수(i-1)에서 +1 연산을 하는 것(즉, i에서 -1 연산을 해서 i-1이 되므로)
  dp[i] = dp[i-1] + 1

  # i가 2으로 나누어 지는 수 라면 2로 나눈 값을 만드는 방법의 수(dp[i//2])에 연산횟수 +1을 한다.
  if i % 2 == 0:
    dp[i] = min(dp[i//2]+1, dp[i])
  
  # i가 3으로 나누어 지는 수 라면 3으로 나눈 값을 만드는 방법의 수(dp[i//3])에 연산횟수 +1을 한다.
  if i % 3 == 0:
    dp[i] = min(dp[i//3]+1, dp[i])
print(dp[n])
'''