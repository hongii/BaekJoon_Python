# 세 번째 코드 -> correct, 이번엔 아예 R이 등장한 총 횟수를 구하고, 마지막에 이 값이 홀수인 경우에만 뒤집어줌.
# 대신, 현재 수행할 함수가 "D"인 경우에 여태 등장한 R의 횟수가 홀수라면 배열을 뒤집은 것 처럼 생각해서 맨 앞 원소가 아닌 맨 뒤 원소를 제거함
# 마지막에 "RRRRDR"과 같이, D가 나온 후 R로 끝나는 경우에는 배열을 뒤집어야 할지 말지 한번 더 확인해주어야 하므로 마지막 else구문에 if reverseCnt % 2 != 0: 조건 추가
from collections import deque
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")

input = sys.stdin.readline
T = int(input())

while T:
  T -= 1
  funcs = input().rstrip()
  n = int(input())
  arr = deque([x for x in input().rstrip()[1:-1].split(",") if x != ""])

  reverseCnt = 0
  for i in range(len(funcs)):
    if funcs[i] == "R":
      reverseCnt += 1

    elif funcs[i] == "D":
      if arr:
        if reverseCnt % 2 != 0: # 여태 등장한 R의 횟수가 홀수개인 경우
          if arr:
            arr.pop() # 배열을 뒤집은 상태라고 가정하고 원소를 하나 제거하는데, 이 때 실제로는 배열을 뒤집지 않았으므로 arr의 마지막원소를 제거
        else: 
          arr.popleft()
      else: # 배열이 비어있으므로 제거하지 못함. 실행 종료
        print("error")
        break
  else:
    if reverseCnt % 2 != 0:
      arr.reverse()
    print("["+ ",".join(list(arr)) + "]")


'''
# arr = [x for x in input()[1:-1].split(",") if x != ""]  코드 설명
=> ex) "[2, 3, 4]"의 형태로 입력받은 문자열 배열을 양쪽 대괄호를 없애고(input()[1:-1]) ","단위로 split를 수행하면(split(",")), 
        ["2", "3", "4"]라는 배열이 만들어짐.(input()[1:-1].split(",") 의 결과물)
        여기서 반복문과 조건문을 통해 빈 문자열만 있는 경우는 빈 배열이 생성되고 숫자 문자열은 배열에 넣어준다.
'''


'''두 번째 코드 -> 시간초과, 반복문 안에서 reverse()를 아예 수행하면 안되는 듯
현재 수행할 함수가 "D"인 경우, 연속해서 나온 R의 갯수가 홀수일때만 배열을 뒤집어 줬는데 이것 또한 시간 초과..
그래서 배열 뒤집는 연산을 아예 수행하지 않고 제거하는 방법이 필요함 -> 세번째 코드 

import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

while T:
  T -= 1
  funcs = input().rstrip()
  n = int(input())
  arr = deque([x for x in input().rstrip()[1:-1].split(",") if x != ""])

  check, reverseCnt = False, 0
  for i in range(len(funcs)):
    if funcs[i] == "R":
      if check:
        reverseCnt += 1
        continue
      else:
        check = True
        reverseCnt += 1

    elif funcs[i] == "D":
      if check:
        if reverseCnt % 2 != 0: # 연속해서 나온 R이 홀수개인 경우, arr 뒤집어줌. 짝수개면 현재 배열 그대로 유지
          arr.reverse()
          check = False
          reverseCnt = 0
      if arr:
        arr.popleft()
      else:
        print("error")
        break
  else:
    if check and reverseCnt % 2 != 0:
      arr.reverse()
    print("["+ ",".join(list(arr)) + "]") # 출력 형태 주의!!!!!!! 원소와 콤마사이 공백 없음. 즉, 문자열로 출력해야함
'''


''' 첫번째 코드 -> 시간초과, R이 등장할 때 마다 매번 reverse()연산 수행해서 시간초과 발생
input = sys.stdin.readline
T = int(input())

while T:
  T -= 1
  funcs = input().rstrip()
  n = int(input())
  arr = deque([int(x) for x in input().rstrip()[1:-1].split(",") if x != ""])
  
  for i in range(len(funcs)):
    if funcs[i] == "R":
      arr.reverse() #  매번 뒤집는 연산을 수행하니 시간초과 발생
    elif funcs[i] == "D":
      if arr:
        arr.popleft()
      else:
        print("error")
        break
  else:
    print(list(arr)) # 이 부분도 출력 결과에선 [1, 2, 3]이 아니라 [1,2,3] 으로 출력해야함 -> 수정 필요
'''