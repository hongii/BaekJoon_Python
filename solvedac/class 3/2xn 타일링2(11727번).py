# 정답 풀이 참고
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")
input = sys.stdin.readline

n = int(input())
dp = [0]*(n+2)
dp[1] = 1
dp[2] = 3
for i in range(3, n+1):
  dp[i] = dp[i-1] + 2*dp[i-2]
print(dp[n]%10007)