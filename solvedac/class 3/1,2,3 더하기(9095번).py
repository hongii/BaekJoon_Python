# 알고리즘 - DP
# 두번째 풀이 - DP이용
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")
input = sys.stdin.readline

T = int(input())

while T:
  T -= 1
  n = int(input())
  dp = [0]*(n+3) # n = 1~3 이하의 값이 나왔을 때 바로 아래의 코드에서 indexError 안나기 위해 n+3으로 넉넉히 잡음
  dp[1], dp[2], dp[3] = 1, 2, 4
  for i in range(4, n+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
  print(dp[n])



'''
# 첫번째 풀이 -> correct, dfs이용
input = sys.stdin.readline

T = int(input())
arr = [1, 2, 3]
def dfs(n, x):
  global cnt
  for num in arr:
    if num + x < n:
      dfs(n, num+x)
    elif num + x == n:
      cnt += 1
    elif num + x > n:
      return

while T:
  T -= 1
  n = int(input())
  cnt = 0
  dfs(n, 0)
  print(cnt)
'''