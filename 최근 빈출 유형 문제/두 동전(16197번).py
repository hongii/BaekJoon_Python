# 수정에 수정을 거친 두번째 코드 
from collections import deque
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\최근 빈출 유형 문제\\input.txt"
sys.stdin = open(filePath, "rt")

row, col = map(int, input().split())
board = []
coins = []
for i in range(row):
  tmp = list(input())
  board.append(tmp)
  if "o" in tmp:
    for j in range(len(tmp)):
      if tmp[j] == "o":
        coins.append((i, j)) # 튜플로 넣어줌

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res, flag = 0, 0
dq = deque()
dq.append((coins[0][0], coins[0][1],coins[1][0],coins[1][1], 0)) # 좌표값들과 cnt값을 튜플로 넣어줌
while dq:
  i1, j1, i2, j2, cnt = dq.popleft()
  if cnt >= 10:
    res = -1
    break

  for i in range(4):
    x1, y1 = i1 + dx[i], j1 + dy[i]
    x2, y2 = i2 + dx[i], j2 + dy[i]
    if not(0 <= x1 < row and 0 <= y1 < col) and not(0 <= x2 < row and 0 <= y2 < col):
      continue

    elif not(0 <= x1 < row and 0 <= y1 < col) or not(0 <= x2 < row and 0 <= y2 < col):
      res = cnt + 1
      flag = 1
      break

    elif 0 <= x1 < row and 0 <= y1 < col and 0 <= x2 < row and 0 <= y2 < col:
      if board[x1][y1] == "#":
        x1, y1 = i1, j1
      if board[x2][y2] == "#":
        x2, y2 = i2, j2
      dq.append((x1, y1, x2, y2, cnt+1))
  if flag:
    break

print(res)

''' 
★ 튜플의 장단점 정리 ★
# 장점: 적은 메모리 공간을 차지한다, 생성 시간이 빠르다, 인덱스를 사용하여 데이터에 접근하는 시간이 짧다(반복문에서의 속도가 빠름) 
# 단점: 데이터 값을 변경할 수 없다, 데이터를 추가하거나 삭제할 수 없다, sorted()메소드를 사용하여 요소들을 정렬할 수 없다.
'''


''' 첫번째 코드 -> WA
# 맞왜틀 엄청했는데 배열 복사 부분에서 틀림 
# cf) 매번 리스트를 만들어 주면서 넣으면 시간 오래 걸림, dq에 넣을때 좌표값만 넣어주자 & 리스트 보다는 튜플의 생성 및 순환 속도도 빠르고 메모리 공간도 더 적게 차지한다. 
#    => 따라서, 값의 수정이 필요 없는 경우 리스트 대신 튜플을 사용하자

row, col = map(int, input().split())
board = []
coins = []
for i in range(row):
  tmp = list(input())
  board.append(tmp)
  if "o" in tmp:
    for j in range(len(tmp)):
      if tmp[j] == "o":
        coins.append([i, j])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res, flag = 0, 0
dq = deque()
dq.append([*coins, 0])
while dq:
  site1, site2, cnt = dq.popleft()
  if cnt >= 10:
    res = -1
    break

  for i in range(4):
    x1, y1 = site1[0] + dx[i], site1[1] + dy[i]
    x2, y2 = site2[0] + dx[i], site2[1] + dy[i]
    if not(0 <= x1 < row and 0 <= y1 < col) and not(0 <= x2 < row and 0 <= y2 < col):
      continue

    elif not(0 <= x1 < row and 0 <= y1 < col) or not(0 <= x2 < row and 0 <= y2 < col):
      res = cnt + 1
      flag = 1
      break

    elif 0 <= x1 < row and 0 <= y1 < col and 0 <= x2 < row and 0 <= y2 < col:
      tmp1, tmp2 = site1, site2 # 문제의 구간 -> 배열 복사 부분
      if board[x1][y1] != "#":
        tmp1 = [x1, y1]
      if board[x2][y2] != "#":
        tmp2 = [x2, y2]
      if tmp1 == site1 and tmp2 == site2:
        continue
      dq.append([tmp1, tmp2, cnt+1])
      
  if flag:
    break

print(res)
'''