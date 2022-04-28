# N x N 미로 ,도착할 수 있으면 1, 아니면 0을 출력한다.
# start 2, 
# finish 3 
# path 0 
# wall 1
# 

import sys

sys.stdin = open("input.txt")

#다음 이동 경로가 미로 밖으로 나가지 않는지 체크 
def isSefeDir(x,y):
    result = False 
    if x < 0 or y < 0 or x >= N or y >= N:
         result = True
    return result 


T = int(input())

for test_case in range(1, T + 1):
    dir = [(-1,0),(1,0),(0,-1),(0,1)]
    x_ = 0
    y_ = 0
    
    N = int(input()) # size of maze
    maze = []
    stack = []
    for i in range(0,N):
        maze.append(list(map(int, input())))
    
    # 시작점 구하기. 
    for  x in range(0,N):
        for y in range(0,N):
            if maze[x][y] == 2:
                x_ = x 
                y_ = y
    # stack.append()
    for x, y in dir:
        
 