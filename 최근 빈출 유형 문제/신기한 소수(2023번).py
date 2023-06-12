# 두번째 코드 -> dfs
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\최근 빈출 유형 문제\\input.txt"
sys.stdin = open(filePath, "rt")

n = int(input())
res = []
def isPrime(x):
  if x == 1:
    return False
  for i in range(2, int(x**0.5)+1):
    if x % i == 0:
      return False
  else:
    return True

def dfs(x):
  if len(x) == n:
    res.append(int(x))
  else:
    for i in range(1, 10):
      if isPrime(int(x + str(i))):
        dfs(x+str(i))

startNum = [2, 3, 5, 7]
for start in startNum:
  dfs(str(start))
for num in res:
  print(num)


'''첫번째 코드 -> 시간 초과, 입력값이 최대 8자리 숫자가 가능하므로 ..
n = int(input())
start = 10**(n-1)
end = 10**n - 1
prime = set()

def isPrime(x):
  if x == 1:
    return False
  for i in range(2, int(x**0.5)+1):
    if x % i == 0:
      return False
  else:
    return True

check = False
res = []
for i in range(start, end+1):
  l = len(str(i))
  for j in range(1, l+1):
    num = int(str(i)[:j])
    if num in prime:
      continue
    else:
      check = isPrime(num)
      if check:
        prime.add(num)
      else:
        break
  else:
    res.append(i)
for num in res:
  print(num)
'''