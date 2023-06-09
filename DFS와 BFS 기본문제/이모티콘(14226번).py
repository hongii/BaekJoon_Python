# 두번째 풀이 -> bfs + dp 이용 : bfs로 모든 경우의 수를 구하고 2차원 dp 테이블에 저장하면서 중복 연산은 피한다.
from collections import deque
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\DFS와 BFS 기본문제\\input.txt"
sys.stdin = open(filePath, "rt")
s = int(input())
dp = [[float('inf')]*(s+1) for _ in range(s+1)] # dp[바탕화면 이모티콘 수][클립보드 이모티콘 수] = 걸린 시간. 
                                                # 즉, dp[i][j] = t의 의미는 바탕화면에 이모티콘 갯수가 i개이고 클립보드에 이모티콘 수가 j개일 때의 걸린 시간(t)
dp[1][0] = 0 # 초기에 바탕화면에 이모티콘 1개가 존재하고 클립보드는 비어있다. 이때 시간은 0초

def bfs():
  dq = deque()
  dq.append([1, 0]) # [바탕화면 이모티콘 수, 클립보드 이모티콘 수]

  while dq:
    screen, clip = dq.popleft()
    if screen == s:
      return dp[screen][clip]
    

    # 바탕화면 이모티콘 한개 삭제하는 연산
    if screen >= 1 and dp[screen-1][clip] == float('inf'):
      dq.append([screen-1, clip])
      dp[screen-1][clip] = dp[screen][clip] + 1

    # 바탕화면에 있는 이모티콘을 클립보드로 복사 -> 주의! 이때 바탕화면에 있는 이모티콘을 클립보드로 복사할때는 이전에 클립보드에 존재하는 내용은 덮어쓰기로 된다. 
    # 즉, 클립보드에 존재하던 이모티콘은 무시되고 지금 복사되는 바탕화면 이모티콘 갯수만큼 클립보드에 새로 덮어쓰기됨. (dp[screen][screen] = dp[screen][clip] + 1)
    if screen <= s and dp[screen][screen] == float('inf'):
      dq.append([screen, screen])
      dp[screen][screen] = dp[screen][clip] + 1

    # 클립보드에 있는 이모티콘을 바탕화면으로 복사 
    if screen+clip <= s and dp[screen+clip][clip] == float('inf'):
      dq.append([screen+clip, clip])
      dp[screen+clip][clip] = dp[screen][clip] + 1

print(bfs())



'''
# 첫번째 풀이 -> dp로만 풀어봤는데..예제는 맞았는데 WA 받음, 반례 통과 못함
s = int(input())
dp = [10e9]*(s+1)
dp[0], dp[1] = 0, 0
for i in range(1, s+1):
  for j in range(i, s+1, i):
    if i == j:
      continue
    elif j == i*2:
      dp[j] = min(dp[j], dp[j-i] + 2)
    else:
      dp[j] = min(dp[j], dp[j-i] + 1)
print(dp, dp[s])
'''