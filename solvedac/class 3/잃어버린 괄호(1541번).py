# 알고리즘 - 그리디 알고리즘
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")

calList = input().split("-") # "-"연산 기호 단위로 나누어 담은 수식, 뺄셈 기호 단위로 괄호를 감싸서 계산한다.
subtractList = [] # 여기에 담긴 숫자들은 뺄셈을 수행해야 하는 숫자들
for s in calList:
  nums = s.split("+")
  tmp = 0
  for x in nums:
    tmp += int(x)
  subtractList.append(tmp)

res = subtractList[0]
for i in range(1, len(subtractList)):
  res -= subtractList[i]
print(res)

'''
ex) input = "50-55+40+31-20+10-100" 이고 이를 뺼셈 연산 기호 단위로 나누어 담으면,
calList = ["50", "55+40+31", "20+10", "100"] 이 된다. 즉, 50-(55+40+31)-(20+10)-(100) 이런식으로 계산을 수행하면 된다.
위의 코드를 수행하고 나면 subtractList = [50, 126, 30, 100]이 되고,
50-126-30-100을 계산하면, res = -206이 된다.


'''