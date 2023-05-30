# import sys
# filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\약점 체크\\input.txt"
# sys.stdin = open(filePath, "rt")

# sol_1) 첫번째 코드 -> 통과, 2차원 배열 이용하여 구현
h, w = map(int, input().split())
world = [[1]*w for _ in range(h)]
heights = list(map(int, input().split()))
for k in range(w):
    cnt = heights[k]
    for i in range(h-1, -1, -1):
        if cnt > 0:
            world[i][k] = 0
            cnt -= 1

res = 0
for i in range(h):
    isStart = False
    cnt = 0
    for j in range(w):
        if world[i][j] == 0:
            if not isStart:
                isStart = True
            elif isStart and world[i][j-1] != 0:
                res += cnt
                cnt = 0
        elif isStart and world[i][j] == 1:
            cnt += 1
print(res)
    


# so1_2) 정답 풀이 -> heights배열만으로 해결 가능
#  현재 위치(i)를 기준으로 왼쪽과 오른쪽에서 각각 가장 높은 height(left_maxH, right_maxH)를 구하고,
#  이 두 max height 중에서 더 낮은 높이(lower_height)를 구한다.
#  이제, 이 lower_height와 비교해서 현재 위치의 높이(height[i])가 더 낮다면, 그 차이만큼 더해주면 된다.(빗물이 고이는 영역)
h, w = map(int, input().split())
heights = list(map(int, input().split()))
res = 0
for i in range(1, w-1): # 양 끝쪽은 빗물이 고일 수 없는 영역이므로 1 ~ w-1까지 순회
    left_maxH = max(heights[:i]) # 현재 위치 i를 기준으로, 왼쪽 영역에서 max 높이 구하기
    right_maxH = max(heights[i+1:]) # 현재 위치 i를 기준으로, 오른쪽 영역에서 max 높이 구하기
    
    lower_height = min(left_maxH, right_maxH)
    if heights[i] < lower_height:
        res += lower_height - heights[i]
print(res)