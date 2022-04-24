# [입력]
#  첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
# 테스트 케이스 별로 책의 전체 쪽 수 P, A, B가 찾을 쪽 번호 Pa, Pb가 차례로 주어진다. 1<= P, Pa, Pb <=1000
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, A, B, 0 중 하나를 출력한다.
import sys

sys.stdin = open("input.txt")

T = int(input())
for test_case in range(1, T + 1):
    
    a_rlt = 0
    b_rlt = 0
     
    P, Pa, Pb = map(int,input().split())
    
        # 최초 검색 시, 왼쪽은 페이지의 시작, 오른쪽은 페이지의 끝으로 설정 . 
    left = 1 
    right = P 
    while True:
        a_rlt += 1
        middle = int((left+right)/2)        
            
        if Pa == middle:
            break
        elif Pa > middle: 
            left = middle
        elif Pa < middle:
            right = middle
            
    left = 1 
    right = P 
    while True:
        b_rlt += 1 
        middle = int((left+right)/2) 
        
        if Pb == middle:
            break
        elif Pb > middle: 
            left = middle
        elif Pb < middle:
            right = middle
            
    result = ''
    if a_rlt < b_rlt:
        result = 'A'
    elif a_rlt > b_rlt:
        result = 'B'
    elif a_rlt == b_rlt:
        result = '0'

    print(f"#{test_case} {result}")
            
  
            
            
            
        
            
       

    
