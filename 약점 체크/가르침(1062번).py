# 두번째 코드 -> 다른 사람 풀이 참고
# 정석 풀이 : 백트래킹 or 비트마스킹으로 해결 가능
# 두번째 풀이에서는, 가르칠 수 있는 단어의 조합과 부분집합을 이용하여 풀이한 코드 
from itertools import combinations
import sys
filePath = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\백준\\BaekJoon\\약점 체크\\input.txt"
sys.stdin = open(filePath, "rt")
n, k = map(int, input().split())
if k < 5:
    print(0)

else:
    remain = k-5
    default_char = set(["a", "n", "t", "i" , "c"])
    remain_alpha = [chr(i) for i in range(ord('a'), ord('z')+1) if chr(i) not in default_char]

    words = []
    for _ in range(n):
      str = input()
      words.append(set(str)-default_char) # 주어진 단어 중에서 필수로 가르쳐야하는 글자 5개를 제외한 나머지 글자의 set을 words리스트에 넣어준다.

    maxCnt = 0
    possible_cb = list(combinations(remain_alpha, k-5)) # default_char를 제외하고 가르칠 수 있는 글자들(remain_alpha) 중에서 k-5개로 만들 수 있는 조합
    for cb in possible_cb:
        cb = set(cb)
        cnt = 0 # 해당 조합으로 가르칠 수 있는 단어 갯수
        for word in words: 
            if set(word).issubset(cb): # 해당 글자가 가르칠 수 있는 단어 조합(cb)의 부분집합이라면 cnt + 1
                cnt += 1
        if maxCnt < cnt: # 가능한 조합들 마다 가르칠 수 있는 단어 갯수(cnt)를 구해서 가장 많은 단어를 가르칠 수 있는 조합의 cnt로 maxCnt를 갱신한다.
            maxCnt = cnt
    print(maxCnt)




''' 첫번째 코드 -> wrong answer....
from collections import Counter
n, k = map(int, input().split())
if k < 5: # 가르쳐야 하는 필수 글자(char)가 5개는 되어야 하므로 주어진 k값이 5 미만이면 가르칠 수 있는 단어(word)가 없다.
    print(0)
    exit(0)
    
words = [input() for _ in range(n)]
default_char = set(["a", "n", "t", "i" , "c"]) # 가르쳐야 하는 필수 글자
dic = Counter()
cnt = 0 # 배울 수 있는 단어 갯수
for word in words:
    if word == "antatica": # 주어진 단어가 필수 단어로만 이루어진 경우 -> 배울 수 있는 단어 + 1 해주고 pass
        cnt += 1
        continue
    
    word = set(word[4:-4]) # 단어의 시작("anta")과 끝("tica")을 잘라냄
    if len(word - default_char) < k-5: # 해당 단어를 배우기 위해서 가르쳐야 하는 글자 수가 k-5를 초과하지 않는다면 조건문 수행
        key = tuple(sorted(list(word - default_char)))
        if key not in dic.keys():
            dic[key] = 0
        dic[key] += 1
dic = dic.most_common()
# print(dic)

remain = k - 5 # 가르칠 수 있는 남은 글자수 
for key, value in dic:
    if remain - len(key) >= 0:
        remain -= len(key)
        cnt += value
print(cnt)
'''