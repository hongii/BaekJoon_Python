# 두번째 풀이 -> 그리디 알고리즘
# 문제 속 힌트 : 둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)
# 위의 조건에서 가치가 큰 동전은 가치가 작은 동전들의 배수임을 명시함 -> 그리디 알고리즘 사용 가능함을 파악할 수 있다.
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort(reverse=True)

cnt = 0
for coin in coins:
  if coin > k:
    continue
  else:
    cnt += k//coin
    k %= coin
print(cnt)



'''첫번째 풀이 -> DP, 메모리 초과.. 
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort()
dp = [0]*(k+1)

for i in range(1, k+1):
  if coins[i] > k:
    break
  for j in range(coins[i], k+1):
    dp[j] = min(dp[j], dp[j-coins[i]] + 1)
print(dp[k])

'''