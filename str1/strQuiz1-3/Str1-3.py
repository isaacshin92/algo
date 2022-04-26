# 1. str1과 str2가 주어진다. 
# 2. 문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고
# 3. 그중 가장 많은 글자의 개수를 출력

import sys


def letterCnt(str2, s):
    cnt = 0
    for i in str2:
        if i == s:
            cnt += 1
    return cnt


# sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T + 1):
    str1 = list(input())
    str2 = list(input())
    
    result = 0
    
    for s in str1:
        cnt = letterCnt(str2, s)
        if cnt > result:
            result = cnt
    print(f"#{test_case} {result}")