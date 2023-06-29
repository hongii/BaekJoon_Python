# 알고리즘 - dp / 브루트포스
# 브루트포스 풀이, 다른 사람 풀이 참고
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")
input = sys.stdin.readline

n = int(input())
arr = [1 if (i**0.5) == int(i**0.5) else 0 for i in range(n+1)] # 제곱수는 1로 저장, 제곱수가 아닌 수는 0으로 저장
cnt = 4 # 문제에서 주어진 조건: "모든 자연수는 넷 혹은 그 이하의 제곱수의 합으로 표현할 수 있다고 증명하였다." -> 최대 연산횟수 4회
for i in range(int(n**0.5), 0, -1):
  if arr[n] == 1: # n이 제곱수라면 최소 연산횟수 1회
    cnt = 1
    break
  elif arr[n-(i**2)] == 1: # n에서 int(n**0.5)의 값을 뺀 나머지 수(=n-(i**2))가 제곱수인 경우
                          # ex) 26 = 5^2 + 1^1 -> 26은 i가 5일때 26-5^2 = 1이므로, 나머지 수인 1은 1의 제곱수이므로 최소 연산횟수 2회
    cnt = 2
    break
  else:
    for j in range(int((n-(i**2))**0.5), 0, -1): 
      if arr[(n-i**2) - j**2] == 1: # n에서 int(n**0.5)의 값을 뺀 나머지 수(=n-(i**2))에서 제곱수를 한번 더 뺀 값(=j**2)이 제곱수인 경우
        cnt = 3
        break
print(cnt)

