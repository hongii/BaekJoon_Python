# 알고리즘 - 플로이드-워셜
# 두번째 코드 -> 문제에서 요구하는 것만 구함, 시간 절약
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")
input = sys.stdin.readline

n = int(input())
board = []
for _ in range(n):
  board.append(list(map(int, input().split())))

for k in range(n):
  for i in range(n):
    for j in range(n):
      if board[i][j] == 1 or (board[i][k] == 1 and board[k][j] == 1):
        board[i][j] = 1

for i in range(n):
  print(*board[i])


'''첫번째 코드 -> 플로이드-워셜 이용, i->j로 가는 최소비용을 구하고 이를 문제의 요구에 맞게 변형함, 그러나 굳이 최소비용을 구할 필요가 없으므로 두번째 코드처럼 변형함
import sys
n = int(input())
board = []
for _ in range(n):
  board.append(list(map(int, input().split())))

for i in range(n):
  for j in range(n):
    if board[i][j] == 0:
      board[i][j] = float('inf')

for k in range(n):
  for i in range(n):
    for j in range(n):
      board[i][j] = min(board[i][j], board[i][k] + board[k][j])

for i in range(n):
  for j in range(n):
    if board[i][j] == float('inf'):
      board[i][j] = 0
    elif board[i][j] >= 1:
      board[i][j] = 1
  print(*board[i])
'''
