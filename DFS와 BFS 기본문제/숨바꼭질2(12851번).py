from collections import deque
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\DFS와 BFS 기본문제\\input.txt"
sys.stdin = open(filePath, "rt")

n, k = map(int, input().split())
dq = deque()
visited_time = [100001]*100001
cnt = 0
minTime = 100001
dq.append((n, 0))
while dq:
  now, time = dq.popleft()
  if time > minTime:
    break
  
  if now == k and time <= minTime:
    minTime = time
    cnt += 1
    continue
  
  for x in [now-1, now+1, now*2]:
    if 0 <= x < 100001 and visited_time[x] >= time+1:
      visited_time[x] = time+1
      dq.append((x, time+1))

print(minTime)
print(cnt)


'''수정과정 거친 초기 코드 -> WA
from collections import deque
n, k = map(int, input().split())
dq = deque()
visited = [False]*100001
visited[n] = True
cnt = 0
minTime = 100001
dq.append((n, 0))
while dq:
  now, time = dq.popleft()
  if time > minTime:
    break
  
  if now == k and time <= minTime:
    minTime = time
    cnt += 1
    continue
  
  for x in [now-1, now+1, now*2]:
    if x == k or (0 <= x < 100001 and not visited[x]):
      visited[x] = True
      dq.append((x, time+1))

print(minTime)
print(cnt)

※ 틀린 이유?
=> x가 이미 등장한적 있는 번호(visited[x] == True)면 검사 안하고 바로 패스시켜 버리는 조건문 때문에 틀림. 
즉, 단순히 방문한 적 있냐 없냐로 따지면 안되고 이미 등장한 적 있는 번호라고 하더라도 동일한 depth인 경우엔 dq에 넣어줘야함

반례)
n=1 k=10 인 경우
(now-1, now+1, now*2 순으로 가지치기, 0 <= x < 100001범위 이내의 값만 표시, 범위 외 값은 x표시)
                                                                                        1                                                    time = 0 (depth = 0)
                                                              0                         2                              2                     time = 1 (depth = 1)
                                                      x       1       0        1        3        4            1        3        4            time = 2 (depth = 2)
                                                           0  2  2          0  2  2  2  4  6  3 (5)  8     0  2  2  2  4  6  3 (5)  8        time = 3 (depth = 3)
                                                                                              4  6  10*                      4  6  10*       time = 4 (depth = 4)
                                                                                                    ↑ cnt+=1                       ↑ cnt+=1
                                                                                              이와 같이 동일한 depth에 존재하는 값이 여러개인 경우가 있기 때문에, 
                                                                                              x값이 (5)인 경우로 예를 들면(depth=3 일때의 x=5인 경우), 
                                                                                              visited[5]를 방문 했냐 안했냐로 따지게 되면 뒤에서 한번 더 등장하는 (5)에 대해서는 
                                                                                              cnt를 증가시키지 않고 넘어가게 되므로 오답이 된다. 
                                                                                              따라서, 단순히 방문 여부를 따지는 것이 아니라 이미 등장한 값 x에 대해서는 같은 depth인 경우에, x를 dq에 넣어줘야 한다.
'''