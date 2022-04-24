# 재귀함수를 통한 재구현. 
# 실행 시간 : 0.11846s
import sys



def search(page_total, index):
    left = 1
    right = page_total
    result = 0
    
    while True:
        result += 1 
        middle = int((left + right)/2)
        if index > middle: 
            left = middle
        elif index < middle: 
            right = middle
        elif index == middle: 
            break
    return result   




sys.stdin = open("input.txt")

T = int(input())
for test_case in range(1, T + 1):
    page_total, pa, pb = map(int, input().split())
    
    a_result = search(page_total, pa)
    b_result = search(page_total, pb)
    
    result = ''
    
    if a_result > b_result:
        result = 'B'
    elif b_result > a_result:
        result = 'A'
    else:
        result = '0'
    print(f"#{test_case} {result}")