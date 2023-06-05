# 다시 풀어보기
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\알고리즘 다지기 기초\\input.txt"
sys.stdin = open(filePath, "rt")
n = int(input())
house = []
for i in range(n):
  house.append(list(map(int, input().split())))

dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)] # 가로, 대각선, 세로 방향의 경우의 수를 각각 담기 위한 3차원 배열

# 파이프는 항상(0,0)과(0,1)위치를 걸치는 가로모양으로 시작한다.
dp[0][0][1] = 1 # (0, 1)위치에 걸치는 가로 파이프 경우의 수
for col in range(2, n):
  if house[0][col] == 0: 
    dp[0][0][col] = dp[0][0][col-1]

for row in range(1, n):
  for col in range(1, n):
    # 가로, 세로 파이프 경우의 수 구하기
    if house[row][col] == 0:
      dp[0][row][col] = dp[0][row][col-1] + dp[2][row][col-1] # 가로
      dp[1][row][col] = dp[1][row-1][col] + dp[2][row-1][col] # 세로
    
    if house[row][col] == 0 and house[row-1][col] == 0 and house[row][col-1] == 0:
      dp[2][row][col] =  + dp[0][row-1][col-1] + dp[1][row-1][col-1] + dp[2][row-1][col-1] # 대각선

print(sum(dp[i][n-1][n-1] for i in range(3)))

'''
# 해설 풀이 - 다른 사람 풀이 참고한 링크 : https://velog.io/@eunseokim/BOJ-17070%EB%B2%88-%ED%8C%8C%EC%9D%B4%ED%94%84-%EC%98%AE%EA%B8%B0%EA%B8%B0-1-dp-%ED%92%80%EC%9D%B4-python
dp[0][row][col] = 가로 파이프에 대한 dp
dp[1][row][col] = 세로 파이프에 대한 dp
dp[2][row][col] = 대각선 파이프에 대한 dp
'''

