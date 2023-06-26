import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")
input = sys.stdin.readline

n = int(input())
if n==1:
  print(1)
else:
  dp = [0]*(n+1)
  dp[1] = 1
  dp[2] = 2
  for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2])%10007
  print(dp[n]%10007)

# 프로그래머스 LV 2 : 2 x n 타일링 과 유사한 문제 -> https://github.com/hongii/programmers_python/blob/main/LV%202/2xn%20%ED%83%80%EC%9D%BC%EB%A7%81.py