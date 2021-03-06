# N x N 미로 ,도착할 수 있으면 1, 아니면 0을 출력한다.
# start 2, 
# finish 3 
# path 0 
# wall 1
# 

import sys

sys.stdin = open("input.txt")

#다음 이동 경로가 미로 밖으로 나가지 않는지 체크 
def isSafeDir(y,x):
    result = False 
    if x < 0 or y < 0 or x >= N or y >= N:
         result = True
    return result 

def dfs(y,x):
    global result
    
    if maze[y][x] == 3 or result:
        result = 1
        return
    for i, j in dir:
        dy = y + i
        dx = x + j
        if not isSafeDir(dy,dx):
            
            if maze[dy][dx] != 1: # 지나온 곳이거나, 벽이 아니면 이동 
                maze[y][x] = 1 # 지나온 곳은 벽으로 표기 
                dfs(dy,dx) #재귀함수 호출

T = int(input())

for test_case in range(1, T + 1):
    
    dir = [(1,0),(-1,0),(0,1),(0,-1)]
    
    y_ = 0
    x_ = 0
    result = 0
    
    N = int(input()) # size of maze
    maze = []
    for i in range(0,N):
        maze.append(list(map(int, input())))
    
    # 시작점 구하기. 
    for  y in range(0,N):
        for x in range(0,N):
            if maze[y][x] == 2:
                y_ = y
                x_ = x 
    dfs(y_,x_)
    
    print(f'#{test_case} {result}')         
    
