# 두번째 풀이 -> 수학적 공식으로 L과 R 연산 수행, pypy3로 제출해서 통과
# L과 R연산 시 주의사항 -> ex) 123인 경우, L연산(왼쪽 shift)의 결과가 231이 아니고 1230이 되고, R연산(오른쪽 shift)의 결과는 3012가 된다. 
from collections import deque
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")
input = sys.stdin.readline
T = int(input())

while T:
  T -= 1
  dq = deque()
  check = [False]*10000
  a, b = map(int, input().split())
  dq.append((a, ""))
  while dq:
    num, order = dq.popleft()
    if num == b:
      print(order)
      break
    else:
      d = (num*2) % 10000
      if not check[d]:
        check[d] = True
        dq.append((d, order+"D"))
      
      s = num-1 if num>0 else 9999
      if not check[s]:
        check[s] = True
        dq.append((s, order+"S"))

      l = (num%1000)*10 + num//1000 
      if not check[l]:
        check[l] = True
        dq.append((l, order+"L"))

      r = (num%10)*1000 + num//10
      if not check[r]:
        check[r] = True
        dq.append((r, order+"R"))



'''첫번째 코드 -> 시간초과, L과 R연산때 deque써서 그런듯.. 수학적 공식으로 접근해야 함
from collections import deque
import sys
input = sys.stdin.readline
T = int(input())

def D(num):
  return (num*2) % 10000

def S(num):
  return num-1 if num>0 else 9999

def L(num):
  num = deque(str(num))
  num.append((num.popleft()))
  return int("".join(num))

def R(num):
  num = deque(str(num))
  num.appendleft((num.pop()))
  return int("".join(num))

while T:
  T -= 1
  dq = deque()
  check = [False]*10000
  a, b = map(int, input().split())
  dq.append((a, ""))
  while dq:
    num, order = dq.popleft()
    if num == b:
      print(order)
      break
    else:
      d, s, l, r = D(num), S(num), L(num), R(num)
      if not check[d]:
        check[d] = True
        dq.append((d, order+"D"))
      if not check[s]:
        check[s] = True
        dq.append((s, order+"S"))
      if not check[l]:
        check[l] = True
        dq.append((l, order+"L"))
      if not check[r]:
        check[r] = True
        dq.append((r, order+"R"))

'''