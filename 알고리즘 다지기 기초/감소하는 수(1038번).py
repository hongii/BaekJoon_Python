# 두번째 코드 -> 조합을 이용한 풀이(다른 사람 풀이 참고 링크 - https://ryu-e.tistory.com/59)
from itertools import combinations
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\알고리즘 다지기 기초\\input.txt"
sys.stdin = open(filePath, "rt")

n = int(input())
nums = []
for i in range(1, 11):
  cb = list(combinations(range(0, 10), i))
  for c in cb:
    c = list(c)
    c.sort(reverse=True)
    num = "".join(map(str, c))
    nums.append(int(num))
nums.sort()
print(nums[n] if len(nums)-1 >= n else -1)
'''
두번째 코드 풀이
=> 0~9까지의 숫자들로 이루어진 조합을 구한다. 이때, 조합은 숫자 1개~10개까지의 모든 조합을 구하면 된다.
1. 0~9까지의 숫자들로, 1개~10개의 원소로 이루어진 조합을 모두 구한다.
2. 각 조합마다 내림차순 정렬하여 감소하는 숫자로 만든다.
3. 감소하는 숫자를 담은 리스트를 오름차순 정렬해준다.
4. 문제에서 주어진 n번째 감소하는 수가 존재하면 해당 값을, 없으면 -1을 반환
'''



''' 첫번째 코드 -> 부르트포스, 그냥 감소하는 숫자 나올때마다 배열에 넣어주도록 냅다 반복문 돌림..(당연히 시간초과) 
n = int(input())
decreaseNums = [10e6]*(n+1)
num = 0
for i in range(n+1):
    if len(str(num)) == 1:
        decreaseNums[i] = num
        num += 1
        continue 
    tmp = str(num)
    while int(tmp) < 9876543210:
        for j in range(len(tmp)-1):
            if tmp[j] <= tmp[j+1]:
                tmp = str(int(tmp) + 1)
                break
        else:
            decreaseNums[i] = int(tmp)
            num = int(tmp) + 1
            break
print(decreaseNums[n] if decreaseNums[n] != 10e6 else -1)
'''
