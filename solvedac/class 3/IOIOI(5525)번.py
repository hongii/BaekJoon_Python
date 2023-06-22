import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")

# 두번째 코드 -> 100점
# "IOI" 문자열을 반복할 때 마다 cntIOI += 1을 해주고, cntIOI == n 이 되었을때 주어진 매칭 문자열p와 동일하므로 res += 1을 해준다.
# 이 때, 해당 위치에서부터 다시 cntIOI를 세는것이 아니라(cntIOI = 0) p문자열을 만족하는 부분 문자열의 가장 앞 "IOI"만 한번 빼주면 되므로 cntIOI -= 1을 해줘야한다.
n = int(input())
length = int(input())
s = input()
p = "IO"*n + "I"

i, cntIOI, res = 0, 0, 0
while i < length-1:
  if s[i:i+3] == "IOI":
    i += 2
    cntIOI += 1
    if cntIOI == n:
      cntIOI -= 1
      res += 1
  else:
    cntIOI = 0
    i += 1
print(res)


'''첫번째 코드-> re 라이브러리를 이용한 문자열 매치 찾기, 50점(부분 통과) 나머지 50점은 시간초과
n = int(input())
length = int(input())
s = input()
p = "IO"*n + "I"

cnt = 0
for i in range(length):
  x = re.search(p, s)
  if x == None:
    break
  else:
    cnt += 1
    s = s[x.start()+2:]
print(cnt)

'''