# 문제 풀이 봤는데 이해가 안가서 다음에 다시 보기..
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\DP 강훈련\\input.txt"
sys.stdin = open(filePath, "rt")
n = int(input())
dp = [0]*(n+2)
time_profit = [[0, 0]]
for i in range(n):
  t, p = map(int, sys.stdin.readline().split())
  time_profit.append([t,p])

for i in range(1, n+1):
  t, p = time_profit[i][0], time_profit[i][1]
  if t+i <= n+1:
    dp[i+t] = max(dp[i+t], dp[i]+p)
  dp[i+1] = max(dp[i+1], dp[i])
print(dp[n+1])