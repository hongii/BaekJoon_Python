# 스케줄링 -> 아직 처리되지 않은 item들 중에 가장 나중에 등장하는 item을 제거하는 방식
# 운영체제 페이징 기법 중에 belady's min algorithm에 해당하는 알고리즘
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\약점 체크\\input.txt"
sys.stdin = open(filePath, "rt")
n, k = map(int, input().split())
items = list(map(int, input().split()))
using = [] # 현재 멀티탭을 사용중인 제품 번호를 담는 리스트
change = 0 # 코드 바꾸는 횟수
for i, item in enumerate(items):
    # case1) 멀티탭에 빈 구멍이 있고 현재 item이 멀티탭에 꽂혀있지 않은 경우 -> 그냥 멀티탭에 꽂아주면 됨
    if len(using) < n and item not in using:
        using.append(item)

    # case2) 멀티탭에 빈 구멍이 없고 현재 item이 멀티탭에 꽃혀있지 않은 경우 -> 스케줄링 필요
    elif len(using) == n and item not in using:
        tmp = using.copy() # 최종적으로 tmp에 남아있는 item번호는 멀티탭에서 제거가능한 item(현재 멀티탭에 꽃혀있는 item중에 아직 처리되지 않은 item에 포함되지 않는 item만 남게됨)
        last = 0 # 가장 나중에 등장하는 item을 담을 변수
        for j in range(i+1, k): # 아직 처리되지 않은 item들 순회
            if items[j] in using and items[j] in tmp: # 남아있는 item중에 지금 확인중인 item이 멀티탭에 꽂혀있고 그 item이 멀티탭에 꽂혀 있다는 것을 처음 알게된 경우
                tmp.remove(items[j]) # 제거 가능한 제품리스트에서 해당 item 제외시킴
                last = items[j]
        if len(tmp) == 0 : # 현재 멀티탭에 꽃혀 있는 item들 전부 아직 처리되지 않은 item들에 포함되어 있다면(제거가능한 item이 없다면), 가장 나중에 등장하는 제품 먼저 제거함
            using.remove(last)
        else: # 현재 멀티탭에 꽂혀있는 item들 중에 이후 두번 다시 등장하지 않는 제품들이 있는 경우(tmp에 존재하는 item들), 해당 item 제거
            using.remove(tmp[0])
        using.append(item)
        change += 1
    
    # 나머지 case들 -> 멀티탭에 빈구멍이 없고 현재 item이 멀티탭에 꽂혀있다면 그냥 pass, 멀티탭에 빈 구멍이 있으나 현재 item이 멀티탭에 꽃혀 있다면 그냥 pass
print(change)