# 알고리즘 - 다이나믹 프로그래밍
# 연속 세칸은 밟으면 안된다는 조건때문에 최댓값 갱신을 어떻게 할지 고민하는 시간 오래걸림, 다른사람 풀이 확인 후 다시 품
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")

n = int(input())
stair = [0] + [int(input()) for _ in range(n)]
dp = [0]*(n+1)
dp[1] = stair[1]
if n == 1:
  print(dp[1])
elif n == 2:
  print(dp[1]+stair[2])
else:
  dp[2] = dp[1]+stair[2]
  for i in range(3, n+1):
    dp[i] = max(stair[i]+stair[i-1]+dp[i-3], stair[i]+dp[i-2])  
  print(dp[n])