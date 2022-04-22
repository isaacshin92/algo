import sys

sys.stdin = open('input.txt')



T = int(input())

for test_case in range(1, T + 1):
    num_cnt, section = list(map(int, input().split()))
    num_list = list(map(int, input().split()))
    
    max = 0
    min = 9999999999
    index = 0
    print(f"num_cnt - section + 1 = {num_cnt - section + 1}")
    for i in range(num_cnt - section + 1):
        print(f"i value : {i}")
        temp = 0
        for j in range(0, section):
            print(f"j value : {j}")
            temp += num_list[i + j]
        
        if temp > max:
            max =  temp
        if temp < min:
            min = temp
    rlt = max - min
    print(f"============= ${test_case}")
    print(f"#{test_case} {rlt}")