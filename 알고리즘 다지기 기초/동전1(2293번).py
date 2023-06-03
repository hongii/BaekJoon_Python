# 다이나믹 프로그래밍 -> 냅색 알고리즘 이용(다시 풀어보기)
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\알고리즘 다지기 기초\\input.txt"
sys.stdin = open(filePath, "rt")
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0]*(k+1)
dp[0] = 1
for coin in coins:
    for i in range(coin, k+1):
        dp[i] += dp[i-coin] 
print(dp[k])

'''
# 냅색 알고리즘 풀이
ex) 동전 1, 2, 5를 중복 사용해서 사용한 동전의 합이 10이 되는 경우의 수 구하기
=>                            동전의 합(=i)     0   1   2   3   4   5   6   7   8   9   10 
  ============================================================================================
  1원짜리 동전 사용해서 만든 경우의수(coin=1)     1   1   1   1   1   1   1   1   1   1   1
  2원짜리 동전까지 같이 사용한 경우의수(coin=2)   1   1   2   2   3   3   4   4   5   5   6
  5원짜리 동전까지 같이 사용한 경우의수(coin=5)   1   1   2   2   3   4   5   6   7   8   10
  즉, 동전의 합 i를 만드는 경우의 수 dp[i] = dp[i](현재 동전을 제외했을때 동전의 합i를 만들 수 있는 경우의 수) + dp[i-coin](현재 동전을 포함했을때 동전의 합i를 만들 수 있는 경우의 수)
dp[0] = 1은 동전 1가지로만 만들 수 있는 경우의 수
'''





'''
# 첫번째 코드 -> dfs로 풀었으나 시간 초과 발생
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coinCnt = [0]*n
tmp = set()
def dfs(total):
    global coin, tmp, coinCnt
    if total >= k:
        if total == k:
            tmp.add(tuple(coinCnt))
    else:
        for i, coin in enumerate(coins):
            coinCnt[i] += 1
            dfs(total+coin)
            coinCnt[i] -= 1
dfs(0)
print(len(tmp))
'''