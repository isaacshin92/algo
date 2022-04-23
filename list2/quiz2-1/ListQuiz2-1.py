#색칠하기 

import sys


sys.stdin = open("input.txt")


T = int(input())



for test_case in range(1, T + 1):
    default = [[0 for w in range(10)] for h in range(10)]
    row = int(input())
    cnt = 0 

    for i in range(1,row + 1):     
        row1,col1,row2,col2,color     = map(int,input().split())

        for r in range(row1, row2 + 1):
            for c in range(col1, col2 + 1):
                if color == 1:
                    if  default[r][c] == 0:
                            default[r][c] = 1
                    elif default[r][c] == 2:
                            default[r][c] = 3
                            cnt += 1
                else:
                    if  default[r][c] == 0:
                            default[r][c] = 2
                    elif  default[r][c] == 1:
                            default[r][c] = 3
                            cnt += 1
    print(f"#{test_case} {cnt}")
                            
        
    
        
        
    
    