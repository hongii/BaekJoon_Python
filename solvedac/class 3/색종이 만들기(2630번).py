# 알고리즘 - 분할 정복(재귀)
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")

# 두번째 코드 -> 코드의 간결화
n = int(input())
board = []
whiteCnt, blueCnt = 0, 0
for i in range(n):
  board.append(list(map(int, input().split())))

def divide(x, y, size):
  global whiteCnt, blueCnt
  color = board[x][y] 

  for i in range(x, x+size):
    for j in range(y, y+size):
      if board[i][j] != color:
        size //= 2
        divide(x, y, size)
        divide(x, y+size, size)
        divide(x+size, y, size)
        divide(x+size, y+size, size)
        return
    
  if color == 1:
    blueCnt += 1
  
  elif color == 0:
    whiteCnt += 1


divide(0, 0, n)
print(whiteCnt)
print(blueCnt)


''' 첫번째 코드 -> correct
n = int(input())
board = []
whiteCnt, blueCnt = 0, 0
for i in range(n):
  board.append(list(map(int, input().split())))

def divide(x, y, size):
  global whiteCnt, blueCnt
  if size == 1:
    if board[x][y] == 1:
      blueCnt += 1
    else:
      whiteCnt += 1
    return
  
  isAllOne, isAllZero = True, True
  for i in range(x, x+size):
    if not all(x == 1 for x in board[i][y:y+size]):
      isAllOne = False
    if not all(x == 0 for x in board[i][y:y+size]):
      isAllZero = False
  
  if isAllOne and not isAllZero:
    blueCnt += 1
    return
  
  elif isAllZero and not isAllOne:
    whiteCnt += 1
    return
  
  else:
    size //= 2
    divide(x, y, size)
    divide(x, y+size, size)
    divide(x+size, y, size)
    divide(x+size, y+size, size)


divide(0, 0, n)
print(whiteCnt)
print(blueCnt)
'''