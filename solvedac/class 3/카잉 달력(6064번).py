# 알고리즘 - 수학, 정수론
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")

T = int(input())
while T:
  T -= 1
  M, N, x, y = map(int, input().split())
  while x <= M*N:
    if x%N == y%N:
      print(x)
      break
    x += M
  if x > M*N:
    print(-1)



'''
# 문제 해결 접근 풀이
'x에 m을 계속 더해나간 값' = 'y에 n을 계속 더해나간 값' 일 때가 정답이 되는 해가 된다.
ex) M=10, N=12, x=3. y=9라면,
    x가 3인 해는 3번째, 13번째, 23번째, 33번째... 해이다. 
    y가 9인 해는 9번째, 21번째, 33번째... 해이다.
    이렇게 카잉 달력의 마지막 해는 최대 N*M번 째를 넘지 않는다.

    위의 관계를 식으로 적어보면,
    x에 계속해서 M을 더하는 것을 반복하면서 조건 x % N == y % N 을 만족할 때의 x값이 우리가 구하고자 하는 k번째 해가 된다.
    1) 3 % 12 != 9 % 12
    2) 13 % 12 != 9 % 12
    3) 23 % 12 != 9 % 12
    4) 33 % 12 == 9 % 12 -> 반복문 탈출, x = 33
    => <3:9>는 33번째 해이다. 

'''