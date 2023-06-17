# 알고리즘 - 브루트포스
# 다른 사람 풀이 참고
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")

n = int(input())
if n == 100:
  print(0)
  sys.exit(0)

m = int(input())
errBtn = []
if m != 0:
  errBtn = list(map(str, input().split()))

cnt = abs(100 - n) # 버튼을 눌러야하는 최대 횟수(+,-버튼으로만 조작할 때 최대 횟수가 된다.)
# 모든 경우의 수를 싹 다 확인하는 브루트포스의 정석..
for num in range(1000000):
  for j in str(num):
    # num에 고장난 버튼을 눌러야 하는 숫자가 포함되어 있다면 pass
    if j in errBtn:
      break
  else:
    cnt = min(cnt, len(str(num))+abs(n-num))
print(cnt)