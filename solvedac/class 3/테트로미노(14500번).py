# 알고리즘 - 구현, 부르트포스
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")
input = sys.stdin.readline

row, col = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row)]

# 테트로미노 블럭의 좌표 경우의 수 19가지. (0, 0)위치 기준으로 테트로미노 좌표 정보를 구함
case = [
    # case 1 : ㅣ모양
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    # case 2 : 정사각형(2*2)모양
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    # case 3 : ㄱ모양
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 0), (1, 0), (0, 1), (0, 2)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (-1, 2)],
    [(0, 0), (0, 1), (-1, 1), (-2, 1)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    # case 4 : 번개 모양
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (-1, 1), (-1, 2)],
    [(0, 0), (0, 1), (-1, 1), (1, 0)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    # case 5 : ㅗ모양
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 0), (-1, 1), (0, 1), (1, 1)],
    [(0, 0), (0, 1), (0, 2), (-1, 1)],
    [(0, 0), (1, 0), (2, 0), (1, 1)]
]

maxSum = 0
def tetromino(x, y):
  global maxSum
  for i in range(19):
    tmpSum = 0
    for j in range(4):
      dx, dy = x + case[i][j][0], y + case[i][j][1]
      if 0 <= dx < row and 0 <= dy < col:
        tmpSum += board[x+case[i][j][0]][y+case[i][j][1]]
    if tmpSum > maxSum:
      maxSum = tmpSum

for i in range(row):
  for j in range(col):
    tetromino(i, j)
print(maxSum)

'''
문제 이해 못해서 풀이 참고함 
i번째 줄의 j번째 수는 위에서부터 i번째 칸, 왼쪽에서부터 j번째 칸에 쓰여 있는 수.. 이 말을 이해못했는데 그냥 (i, j)에 위치한 값이라는 뜻..;
종이 위의 값이라는 말을 못보고 (i, j)에 적힌 숫자값이 높이라고 잘못 이해해서 3차원 배열로 착각함. 그래서 도형을 눕히는게 아니라 세우는 건 줄..
# 풀이 참고 사이트 - https://wisdom-990629.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-14500%EB%B2%88-%ED%85%8C%ED%8A%B8%EB%A1%9C%EB%AF%B8%EB%85%B8
'''