# 다이나믹 프로그래밍 - 냅색 알고리즘
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\알고리즘 다지기 기초\\input.txt"
sys.stdin = open(filePath, "rt")
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [10e6]*(k+1)
dp[0] = 0 # 0원을 만들기 위한 동전의 갯수는 0개로 초기화
for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin]+1) 
print(dp[k] if dp[k] != 10e6 else -1)

# 유사한 문제 - https://github.com/hongii/Python-Algorithom/blob/main/7.%20%EB%8F%99%EC%A0%81%20%EA%B3%84%ED%9A%8D%EB%B2%95/11.%20%EB%8F%99%EC%A0%84%EA%B5%90%ED%99%98(%EB%83%85%EC%83%89%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98).py