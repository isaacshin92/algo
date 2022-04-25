#list 정렬 

from cgitb import small
import sys

sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T + 1):
    
    num_cnt  = int(input())
    num_list = list(map(int,input().split()))
    num_list.sort()
    
    new_list = list()
    result = list()
    
    for i in range(1, (len(num_list) + 2)//2):
    
    # if len(num_list) != 1:
        high_num = num_list[len(num_list) - 1]
        new_list.append(str(high_num))
        num_list.remove(high_num)
        
        low_num = num_list[0]
        new_list.append(str(low_num))
        num_list.remove(low_num)
        
    for i in range(10):
        result.append(new_list[i])
        
    print(f"#{test_case} {' '.join(result)}")
