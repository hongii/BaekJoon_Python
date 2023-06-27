# 두번째 코드 -> 최소힙, 최대힙 두개를 이용하여 최소값 최대값 제거. 두 힙의 요소들의 동기화를 위해 check배열 이용
# 동기화 부분 다른 사람 풀이 참고
import heapq
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\solvedac\\class 3\\input.txt"
sys.stdin = open(filePath, "rt")
input = sys.stdin.readline

T = int(input())
while T:
  T -= 1
  n = int(input())
  maxHq, minHq = [], []
  check = [False]*n
  for i in range(n):
    op, num = input().rstrip().split()
    num = int(num)
    if op == "D":
      if minHq and num == -1:
        # minHq의 첫번째 요소가 이미 최대힙에서 제거된 숫자인 경우, minHq에서도 해당 요소를 제거 -> 동기화 작업
        while minHq and not check[minHq[0][1]]:
          heapq.heappop(minHq)
        
        # 동기화 작업을 끝낸 후, minHq가 비어있지 않다면 min값 제거
        if minHq:
          check[minHq[0][1]] = False
          heapq.heappop(minHq)
      
      elif maxHq and num == 1:
        # maxHq의 첫번째 요소가 이미 최소힙에서 제거된 숫자인 경우, maxHq에서도 해당 요소를 제거 -> 동기화 작업
        while maxHq and not check[maxHq[0][1]]:
          heapq.heappop(maxHq)
        
        # 동기화 작업을 끝낸 후, maxHq가 비어있지 않다면 max값 제거
        if maxHq:
          check[maxHq[0][1]] = False
          heapq.heappop(maxHq)
        
    elif op == "I":
      heapq.heappush(minHq, (num, i))
      heapq.heappush(maxHq, (-num, i))
      check[i] = True
  
  # 모든 연산이 끝난 이후에 마지막으로 동기화 작업수행
  while minHq and not check[minHq[0][1]]:
    heapq.heappop(minHq)
  while maxHq and not check[maxHq[0][1]]:
    heapq.heappop(maxHq)
  
  if maxHq and minHq:
    print(-maxHq[0][0], minHq[0][0])
  else:
    print("EMPTY")


''' 첫번째 코드 -> 시간초과, 최소힙을 하나만 이용하여 구현. but, remove()부분에서 시간초과 나는듯.. 
# 프로그래머스 LV 3 : 이중 우선순위 큐와 유사한 문제 -> https://github.com/hongii/programmers_python/blob/main/LV%203/%EC%9D%B4%EC%A4%91%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84%ED%81%90.py
# 프로그래머스에서 통과된 풀이와 동일하지만 백준에서는 시간초과 -> 프로그래머스 테케가 부족한 듯..
import heapq
import sys
input = sys.stdin.readline

T = int(input())
while T:
  T -= 1
  n = int(input())
  hq = []
  for i in range(n):
    op, num = input().rstrip().split()
    num = int(num)
    if hq and op == "D":
      if num == -1:
        heapq.heappop(hq)
      elif num == 1:
        hq.remove(max(hq)) 
        heapq.heapify(hq)
    elif op == "I":
      heapq.heappush(hq, num)
  if len(hq):
    print(max(hq), hq[0])
  else:
    print("EMPTY")

'''