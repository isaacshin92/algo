#회문 찾기 
#회문은 1 개만 존재하지만, 가로 뿐 아니라 세로로 존재할 수 있다. 
# 소요시간 

import sys

sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T + 1):
    size, target = map(int, input().split())
    board = []
    
    for i in range(size):
        board.append(list(map(str,input().split())))

    
