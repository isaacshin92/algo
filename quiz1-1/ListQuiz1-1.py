import sys

sys.stdin = open('input.txt')



T = int(input())

for test_case in range(1, T + 1):
    
    num = int(input())                        
    num_list = list(map(int, input().split()))
    num_list.sort()
        
    rlt = num_list[num - 1] - num_list[0]
    print(f"#{test_case} {rlt}")
