# 알고리즘 - DP
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")
input = sys.stdin.readline

T = int(input())
while T:
  T -= 1
  n = int(input())
  dp = [0] * (n+5)
  dp[1], dp[2], dp[3], dp[4], dp[5] = 1, 1, 1, 2, 2
  for i in range(6, n+1):
    dp[i] = dp[i-5] + dp[i-1]
  print(dp[n])

'''
이번 문제는 이미 문제에서 규칙을 유도하도록 값을 준 문제라 아주 쉽게 dp 점화식을 알아차릴 수 있었음
=> "파도반 수열 P(N)은 나선에 있는 정삼각형의 변의 길이이다. P(1)부터 P(10)까지 첫 10개 숫자는 1, 1, 1, 2, 2, 3, 4, 5, 7, 9이다."
    즉, dp[n]은 n번째 나선 삼각형의 한 변의 길이
'''