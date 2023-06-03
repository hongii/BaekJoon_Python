import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\알고리즘 다지기 기초\\input.txt"
sys.stdin = open(filePath, "rt")

n = int(input())
board = []
for i in range(n):
    board.append(list(input()))

def checkMaxCnt():
    res = 0
    # 행 부분 최대 길이 체크
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if board[i][j] == board[i][j+1]:
                cnt += 1
            else:
                cnt = 1
            res = max(res, cnt)

    # 열 부분 최대길이 체크
    for col in zip(*board):
        cnt = 1
        for j in range(len(col)-1):
            if col[j] == col[j+1]:
                cnt += 1
            else:
                cnt = 1
            res = max(res, cnt)
    return res

maxCnt = 0
dx = [0, 1]
dy = [1, 0]
for i in range(n):
    for j in range(n):
        for k in range(2):
            x = i + dx[k]
            y = j + dy[k]
            if 0 <= x < n and 0 <= y < n and board[x][y] != board[i][j]:
                board[i][j], board[x][y] = board[x][y], board[i][j]
                cnt = checkMaxCnt()
                board[i][j], board[x][y] = board[x][y], board[i][j]
                if cnt > maxCnt:
                    maxCnt = cnt
print(maxCnt)


'''
# 첫번째 코드 -> "틀렸습니다"판정 : 맞왜틀 겁나 한 풀이.....
# 문제조건에 "두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다." -> 가장 긴 "연속"부분....연속된 부분....
# 연속한 부분을 구하는거라 단순히 Counter사용해서 갯수만 구하면 안됨..;;
n = int(input())
board = []
for i in range(n):
    board.append(list(input()))

def checkMaxCnt():
    tmp = 0
    for i in range(n):
        counter = Counter(board[i])
        counter = counter.most_common()
        tmp = max(counter[0][1], tmp)

    for col in zip(*board):
        counter = Counter(col)
        counter = counter.most_common()
        tmp = max(counter[0][1], tmp)
    return tmp

maxCnt = 0
dx = [0, 1]
dy = [1, 0]
for i in range(n):
    for j in range(n):
        for k in range(2):
            x = i + dx[k]
            y = j + dy[k]
            if 0 <= x < n and 0 <= y < n and board[x][y] != board[i][j]:
                board[i][j], board[x][y] = board[x][y], board[i][j]
                cnt = checkMaxCnt()
                board[i][j], board[x][y] = board[x][y], board[i][j]
                if cnt > maxCnt:
                    maxCnt = cnt
print(maxCnt)
'''
