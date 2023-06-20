# 알고리즘 - 그리디 알고리즘
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")

n = int(input())
time = []
for _ in range(n):
  start, end = map(int, input().split())
  time.append((start, end))
time.sort(key=lambda x:(x[1], x[0]))

cnt = 1
now = 0
for i in range(1, n):
  if time[now][1] <= time[i][0]:
    cnt += 1
    now = i

print(cnt)

'''
주의!
=> time.sort(key=lambda x:(x[1])) 로만 정렬했을때의 반례
4
3 3
2 3
1 3
2 2

위의 경우 x[1]에 대해서만 오름 차순 정렬하면,
[(2, 2), (3, 3), (2, 3), (1, 3)] 로 정렬되어 cnt = 2가 된다.
회의 끝나는 시간이 여러개가 존재하는 경우 회의 시작 시간이 더 빠른 것이 먼저 오도록 정렬 해야한다.
=> time.sort(key=lambda x:(x[1], x[0])) 이렇게 정렬해야 correct
'''
